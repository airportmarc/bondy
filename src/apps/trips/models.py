from django.db import models
from django.conf import settings

from django.utils import timezone
from src.apps.property.models import Property



from src.core.models import CustomBaseClass

# Create your models here.

class Trip(CustomBaseClass):

    name = models.CharField(max_length=120, blank=True)
    notes = models.CharField(max_length=400, blank=True)
    clients = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ClientsTrip', related_name='clientsontrip')
    tripStart = models.DateTimeField(blank=False)
    agent = models.ForeignKey(settings.AUTH_USER_MODEL)
    property = models.ManyToManyField(Property, through='PropertyOnTrip')
    is_active = models.BooleanField(default=True)

    def status(self):
        output = ''

        if not self.is_active:
            output = "Deleted"
        elif self.tripStart > timezone.now():
            output = 'Active'
        else:
            output = 'Past'

        return output




class ClientsTrip(CustomBaseClass):

    trip = models.ForeignKey(Trip)
    clients = models.ForeignKey(settings.AUTH_USER_MODEL)
    onLease = models.BooleanField(default=False)

class PropertyOnTrip(CustomBaseClass):

    property = models.ForeignKey(Property)
    trip = models.ForeignKey(Trip)



