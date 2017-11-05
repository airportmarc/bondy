from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from src.apps.Profile.models import Agent
import logging

class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)

    # def save_user(self, request, user, form, commit=False):
    #     logging.error("made it to the custom Save_user")
    #     data = form.cleaned_data
    #     user.email = data.get('email')
    #     user.first_name = data.get('first_name')
    #     user.last_name = data.get('last_name')
    #     if 'password1' in data:
    #         user.set_password(data['password1'])
    #     else:
    #         user.set_unusable_password()
    #     if commit:
    #         user.save()
    #     return user

    def save_client_user(self, request,  invite, data,  commit=False):
        user = self.new_user(self, request)

        user.first_name = invite.first_name
        user.last_name = invite.last_name
        user.email = invite.email
        user.set_password(data['password'])
        self.populate_username(self, request, user)

        if commit:
            user.save()
        return user





class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)
