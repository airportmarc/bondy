from django.db import models
from django.conf import settings


from src.core.models import CustomBaseClass
from src.apps.contracts.models import Contract


class BaseTerm(CustomBaseClass):

    text = models.CharField(max_length=500)
    help_text = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)

    pass


class Term(BaseTerm):

    contract = models.ForeignKey(Contract)
    is_current = models.BooleanField(default=True)
    is_displayed = models.BooleanField(default=True)
    revision_history = models.ForeignKey('TermRevisionHistory')


class TemplateTerm(BaseTerm):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)



class TermRevisionHistory(Term):
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL)

