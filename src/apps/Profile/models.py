from django.db import models
from django.conf import settings
from src.core.models import CustomBaseClass,Contact
from django.utils import timezone




class Profile(CustomBaseClass):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birth_date = models.DateField(null=True, blank=True)
    legal_name = models.CharField(max_length=50, blank=True, null=True)
    short_bio = models.CharField(max_length=200, null=True, blank=True)
    is_agent = models.BooleanField(default=False)

    def get_name(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + ' ' + self.user.last_name
        else:
            return self.user.email
    def __str__(self):
        return self.get_name()


class Agent(models.Model):
    """
    When the client accpets the invite, then the user becomes apart of this circle.

    """
    agent_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    clients = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,  through='ClientsOfAgents')
    agent_id = models.CharField(max_length=40, null=True, blank=True)
    brokerage = models.ForeignKey('Brokerage', null=True)


class ClientsOfAgents(CustomBaseClass):

    is_onLease = models.BooleanField(default=False)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='clients')
    agent = models.ForeignKey('Agent')

    def __str__(self):
        return "{} is a client of {}".format(self.client.first_name, self.agent.first_name)



class Brokerage(Contact):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class UserContact(Contact):

    user = models.ForeignKey(Profile)
    move_in_date = models.DateField()
    move_out_date = models.DateField(null=True, default=timezone.now)


class Reference(Contact):
    user = models.ForeignKey(Profile)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    relationship = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.user.get_full_name() + ' Reference from ' + self.first_name


class WorkHistory(Contact):
    user = models.ForeignKey(Profile)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    role = models.CharField(max_length=100, null=True)
    salary = models.CharField(max_length=100, null=True)
    reason_for_leaving = models.CharField(max_length=100, null=True)


class DocumentType(CustomBaseClass):
    """
    What type of Document is this uploaded, ID, bank notice, Credit Score, etc
    """
    documentType = models.CharField(max_length=100)

    def __str__(self):
        return self.documentType


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Document(CustomBaseClass):
    user = models.ForeignKey(Profile)
    document_type = models.ForeignKey(DocumentType)
    document = models.FileField(upload_to=user_directory_path)

