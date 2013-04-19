import re


def clean_names():
    f = open('us_female_dist_', 'r')
    aggregated_names = ""
    for line in f.readlines():
        aggregated_names += re.findall('[a-zA-Z]+', line)[0] + "\n"

    f.close()
    f_new = open('us_female_', 'w')
    f_new.write(aggregated_names)
    f_new.close()


def main():
    if len(sys.argv) < 2:
        sys.exit("Must provide an option")
    else:
        if sys.argv[1] == 'clean':
            clean_names()

if __name__ == '__main__':
    main()
