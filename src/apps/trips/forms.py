
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from .models import Trip

class CreateTripForm(forms.ModelForm):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.field_class = ''
        self.helper.layout = Layout(
            Field('name', placeholder='Give this trip a name'),
            Field('notes', placeholder='Add any notes here'),
            Field('clients', placeholder='Type clients Name', autocomplete='off'),
            Field('tripStart', placeholder='When will you meet', autocomplete='off'),
            Field('property', placeholder='What locations will you visit', autocomplete='off'),
            Submit('Save', 'Save', css_class='btn btn-primary m-b')
        )



    class Meta:
        model = Trip
        fields = ['clients', 'tripStart', 'property', 'name', 'notes']
