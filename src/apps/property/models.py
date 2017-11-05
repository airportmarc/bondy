from django.db import models

from src.core.models import Contact


class PropertyManager(models.Manager):

    def get_or_create_property(self, mls):
        #will always return the object
        p, is_object = self.loaded_or_create(mls)

        if is_object:
            return p

        return self.get_queryset().get(pk=p)


    def loaded_or_create(self, num):
        MLS_CUT = 5
        if len(num) < MLS_CUT:
            # This is the PK, dont add
            return (num, False)
        elif self.get_queryset().filter(mls=num).exists():
            # its a MLS number, but already in the DB, return object
            return (self.get_queryset().get(mls=num), True)
        else:
            #its a new MLS number
            p = self.create(mls=num)
            return (p, True)




# Create your models here.


class Property(Contact):

    mls = models.CharField(max_length=100)

    objects = PropertyManager()

    def add(self, mls, scrape=False):
        self.mls = mls
        self.save()
        if(scrape):
            self.get_mls_data(mls)

    def get_mls_data(self, mls):
        pass

    def __str__(self):
        return self.mls










class Scrape():

    def get_address(self):
        pass

    def get_bedrooms(self):
        pass



