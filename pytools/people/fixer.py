from django.core.management import setup_environ
import people.settings as settings
setup_environ(settings)
from app.models import People, Names
import eventlet
from eventlet.green import urllib2
import sys
import requests
#import grequests
from datetime import datetime
import simplejson

crawled_users = 0


def save_names(file_name):
    f = open('people/names/' + file_name, 'r')
    for line in f.readlines():
        user_name, user_name_created = Names.objects.get_or_create(
            name=line.replace('\n', '').title(),
            gender=file_name.split('_')[1],
            country=file_name.split('_')[0])
        print user_name.name

    return


def clean_names():
    for each_name in Names.objects.all():
        each_name.name = each_name.name.title()
        each_name.save()


def fetch(url):
    try:
        crawled_data = urllib2.urlopen(url["url"]).read()
        result = simplejson.loads(crawled_data)
        print result
        name = url["name"]
        name.crawled = True
        name.success = True
        name.save()
        for each_person in result["data"]:
            person = People.objects.create(name=each_person["name"],
                                           gender=name.gender,
                                           country=name.country)
            person.save()

        return {"name": url["name"], "crawled_users": len(result["data"])}

    except:
        name = url["name"]
        name.crawled = True
        name.success = False
        name.save()
        return {"name": url["name"], "crawled_users": None}


def reset_names():
    Names.objects.filter(crawled=True).update(crawled=False)


def facebook_crawl():
    urls = []
    access_token = "BAACEdEose0cBAOr8YEmUZB7U5vwKyegZCuScYbV7MjsHGlKPkPOx2etyZAlPYwN5jT2zVDyM5u7dEHZBg7PfnUXPQ3Auo2z8UzdZCuDzUn7d0SyxNvJmYGQLSkRR9ycCUZADidoRXULvDbjjjZAzDloT9mqRFtG21JzQQZCSWHCj0EGSaHTFZAM5B3jfCa11g4haYmDkk3pjaBgZDZD"
    for each_name in Names.objects.filter(success=False):
        url = "https://graph.facebook.com/search?q=%(code)s&type=user&access_token=%(access_token)s&limit=100"\
            % {"code": each_name.name, "access_token": access_token}
        urls.append({"url": url, "name": each_name})
    """
    for each_url in urls:
        print each_url
        r = requests.get(each_url)
        print r.text
    return
    """
    global crawled_users
    pool = eventlet.GreenPool(200)
    for body in pool.imap(fetch, urls):
        if body["crawled_users"]:
            crawled_users += body["crawled_users"]

        #print crawled_users
    return


def main():
    if len(sys.argv) < 2:
        sys.exit("Must provide an option")
    else:
        if sys.argv[1] == 'save':
            save_names(sys.argv[2])
        elif sys.argv[1] == 'fbcrawl':
            facebook_crawl()
        elif sys.argv[1] == 'clean':
            clean_names()

if __name__ == '__main__':
    main()
