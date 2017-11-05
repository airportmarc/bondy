from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from allauth.account.utils import complete_signup


from .forms import ClientSignupForm
from src.apps.invite.models import Invite
from src.apps.Profile.models import Agent, ClientsOfAgents
from src.apps.users.adapters import AccountAdapter
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'pk'
    slug_url_kwarg = 'pk'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'pk': self.request.user.pk})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'pk': self.request.user.pk})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(pk=self.request.user.pk)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'pk'
    slug_url_kwarg = 'pk'


class ClientSignup(FormView):
    form_class = ClientSignupForm
    template_name ='account\client_signup.html'
    success_url = reverse_lazy('users:redirect')

    def __int__(self, **kwargs):
        super(ClientSignup, self).__int__(**kwargs)
        self.verified_email = self.get_verified_email()

    def get_initial(self):

        intial = super(ClientSignup, self).get_initial()
        intial['email'] = self.get_verified_email()
        return intial

    def form_valid(self, form):
        cd = form.cleaned_data
        data = {}

        inv = Invite.objects.get(email=cd.get('email'))
        data['password'] = cd.get('password')

        user = AccountAdapter.save_client_user(AccountAdapter, self.request, inv, data, True)

        agent = Agent.objects.get(pk=inv.inviter_id)
        coa = ClientsOfAgents()
        coa.agent = agent
        coa.client = user
        coa.save()

        return complete_signup(self.request, user, settings.ACCOUNT_EMAIL_VERIFICATION, self.get_success_url() )

    def get_verified_email(self):
        return self.request.session.get('account_verified_email', None)








