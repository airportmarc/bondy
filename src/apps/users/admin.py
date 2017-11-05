from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

        exclude = ['username']
        field_classes = []


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_email': 'This email has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password']


    def clean_email(self):
        em = self.cleaned_data["email"]
        try:
            User.objects.get(email=em)
        except User.DoesNotExist:
            return em
        raise forms.ValidationError(self.error_messages['duplicate_email'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    extra = (
        (None, {'fields': ('password',)}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    fieldsets = (
            ('User Profile', {'fields': ('first_name', 'last_name',)}),
    ) + extra
    list_display = ('first_name', 'last_name', 'is_superuser')
    search_fields = ['first_name']
    ordering = ['email']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
