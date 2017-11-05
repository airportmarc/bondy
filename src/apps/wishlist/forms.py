
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from .models import Wish

class CreateWishFrom(forms.ModelForm):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.field_class = ''
        self.helper.layout = Layout(
            Field('property', placeholder='What locations do you visit', autocomplete='off'),
            Submit('Save', 'Save', css_class='btn btn-primary m-b')
        )

    class Meta:
        model = Wish
        fields = ['property']
