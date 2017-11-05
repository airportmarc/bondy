from django.contrib import admin
from . import models


# Register your models here.

myModels = [
    models.Profile,
    models.Agent,
    models.Brokerage,
    models.ClientsOfAgents,
    models.DocumentType,
    models.Document,
    models.UserContact,
    models.Reference,
    models.WorkHistory
]
admin.site.register(myModels)
