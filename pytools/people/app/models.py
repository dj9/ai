from django.db import models

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=1024)
    gender = models.CharField(max_length=10)
    profession = models.CharField(max_length=1024)
    country = models.CharField(max_length=1024)


class Names(models.Model):
    name = models.CharField(max_length=1024)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=1024)
    city = models.CharField(max_length=1024)
    crawled = models.BooleanField(default=False)
    success = models.BooleanField(default=False)


class EntityDescriptor(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(null=True, blank=True)


class Entity(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(null=True, blank=True)


class EntityDescriptorRelation(models.Model):
    entity = models.ForeignKey(Entity)
    relation = models.CharField(max_length=1024)
    entity_descriptor = models.ForeignKey(EntityDescriptor)
    best_description = models.BooleanField(default=False)

class EntityValueEvent(models.Model):
    entity_relation = models.ForeignKey(EntityDescriptorRelation)
    date_of_event = models.DateField(null=True, blank=True)


class EntityValueUnit(models.Model):
    name = models.CharField(max_length=256)


class EntityValueInteger(models.Model):
    entity_relation = models.ForeignKey(EntityDescriptorRelation)
    value = models.IntegerField(default=0)
    unit = models.CharField(max_length=256)
    

class EntityValueFloat(models.Model):
    entity_relation = models.ForeignKey(EntityDescriptorRelation)
    value = models.DecimalField()
    unit = models.CharField(max_length=256)