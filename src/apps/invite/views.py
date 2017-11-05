from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import CreateView
from src.apps.invite.models import Invite
import logging


from .forms import InviteForm

class MakeInviteView(CreateView):
    form_class = InviteForm
    template_name = 'invite/new-invite.html'
    success_url = reverse_lazy('invite:new')

    def form_valid(self, form):
        logging.error("form is valid")
        kwargs = {}


        kwargs['first_name'] = form.cleaned_data.get('first_name')
        kwargs['last_name'] = form.cleaned_data.get('last_name')

        self.object = form.save(commit=False)
        self.object.invite_reason = Invite.TRIBE

        inv = self.object.create(self.object.email, inviter=self.request.user, **kwargs)

        inv.send_invitation(self.request)
        return HttpResponseRedirect(self.get_success_url())





