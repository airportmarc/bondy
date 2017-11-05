"""
This is to supply the new singup page over AllAuths default pages
"""

from django import forms
from django.forms.widgets import CheckboxInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Button, Div
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
import logging
from src.apps.Profile.models import Profile, Agent




class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    agent_id = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__( *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.field_class = ''
        self.helper.layout = Layout(
            Field('first_name', placeholder='First Name', autocomplete='off'),
            Field('last_name', placeholder='Last Name', autocomplete='off'),
            Field('email', placeholder='Email', autocomplete='off'),
            Field('agent_id', placeholder='Agent ID', autocomplete='off'),
            Field('password1', placeholder='Password', autocomplete='off'),
            Div(Submit('Register', 'Register', css_class='btn btn-primary block full-width m-b'), css_class='form-group'),
            HTML('<p class="text-muted text-center"><small>Already have an account?</small></p>'),
            Div(HTML('<a class ="btn btn-sm btn-white btn-block" href="' + reverse('account_login') + ' " > Login </a>'),css_class='form-group' )
        )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        agentId = self.cleaned_data.get('agent_id', None)
        if agentId:
            ap = Agent.objects.create(agent_id=agentId, agent_profile=user.profile)



class ClientSignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, **kwargs):
        super(ClientSignupForm, self).__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.field_class = ''
        self.helper.layout = Layout(
            Field('email', placeholder='Email', readonly=True, autocomplete='off'),
            Field('password', placeholder='Password', autocomplete='off'),
            Submit('Register', 'Register', css_class='btn btn-primary m-b')
        )


#
# class ContactDetailsForm(forms.ModelForm):
#
#
#     def __init__(self, *args, **kwargs):
#         super(ContactDetailsForm, self).__init__(*args, **kwargs)
#
#         self.helper = FormHelper(self)
#         self.helper.form_class = 'form-inline'
#         self.helper.form_id = 'addNewAddress'
#         self.helper.disable_csrf = False
#         self.helper.label_class = 'col-sm-4'
#         self.helper.field_class = 'col-sm-4'
#         self.helper.form_tag = False
#         self.helper.layout = Layout(
#             HTML("<div class='hidden' id='addressDate'>"),
#             'is_current',
#             Field('start_date', data_provider='datepicker', css_class='datepicker'),
#             Field('end_date', data_provider='datepicker', css_class='datepicker'),
#             Field('address_1', data_geo='route'),
#             Field('country', data_geo='country'),
#             Field('city', data_geo='locality'),
#             Field('postal_code', data_geo='postal_code'),
#             Field('state', data_geo='administrative_area_level_1'),
#             HTML("</div>")
#
#         )
#
#     class Meta:
#         model = ContactDetails
#         fields = ['address_1', 'country', 'state', 'city', 'postal_code',
#                   'is_current', 'start_date', 'end_date']
#         widgets = {
#             'is_current': CheckboxInput()
#         }



