from django.db import models
from django.conf import settings

from src.apps.property.models import Property

# Create your models here.


class Wish(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    property = models.ForeignKey(Property)



