from django.db import models
from django.conf import settings
from src.core.models import CustomBaseClass

# Create your models here.


class BaseContract(CustomBaseClass):
    name = models.CharField(max_length=100)
    contract_type = models.ForeignKey('ContractType')


class Contract(BaseContract):
    pass





class TemplateContract(BaseContract):
    pass





class ContractType(CustomBaseClass):
    OPTIONS = [
        ('lease', 'Lease'),
        ('Form2', 'Realitor Form')
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=OPTIONS)
    desc = models.CharField(max_length=1000)


class Lease(Contract):
    pass
