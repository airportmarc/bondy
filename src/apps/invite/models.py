import datetime
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _

from invitations.app_settings import app_settings
from invitations.base_invitation import AbstractBaseInvitation
from invitations import signals
from invitations.adapters import get_invitations_adapter





class Invite(AbstractBaseInvitation):
    TRIBE = 'circle'
    AGENT_TO_LEASE = 'agent'

    INVITE_REASON_CHOICE = [
        (TRIBE, 'Join my circle'),
        (AGENT_TO_LEASE, 'Get other agent onto Lease')
    ]
    email = models.EmailField(unique=True, verbose_name=_('e-mail address'),
                              max_length=app_settings.EMAIL_MAX_LENGTH)

    created = models.DateTimeField(verbose_name=_('created'),
                               default=timezone.now)

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=40)
    invite_reason = models.CharField(max_length=40, choices=INVITE_REASON_CHOICE)
    invite_reason_value = models.CharField(max_length=150, null=True, blank=True)

    @classmethod
    def create(cls, email, inviter=None, **kwargs):
        key = get_random_string(64).lower()
        instance = cls._default_manager.create(
            email=email,
            key=key,
            inviter=inviter,
            **kwargs)
        return instance

    def key_expired(self):
        expiration_date = (
            self.sent + datetime.timedelta(
                days=app_settings.INVITATION_EXPIRY))
        return expiration_date <= timezone.now()

    def send_invitation(self, request, **kwargs):
        current_site = (kwargs['site'] if 'site' in kwargs
                        else Site.objects.get_current())
        invite_url = reverse('invitations:accept-invite',
                             args=[self.key])
        invite_url = request.build_absolute_uri(invite_url)

        ctx = {
            'invite_url': invite_url,
            'site_name': current_site.name,
            'email': self.email,
            'key': self.key,
            'inviter': self.inviter,
        }

        email_template = 'invitations/email/email_invite'

        get_invitations_adapter().send_mail(
            email_template,
            self.email,
            ctx)
        self.sent = timezone.now()
        self.save()

        signals.invite_url_sent.send(
            sender=self.__class__,
            instance=self,
            invite_url_sent=invite_url,
            inviter=self.inviter)

    def __str__(self):
        return "Invite: {0}".format(self.email)
