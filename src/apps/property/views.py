from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

from .models import Property
from .forms import CreatePropertyForm

class CreateProperty(CreateView):
    template_name = 'property\create.html'
    model = Property
    form_class = CreatePropertyForm
    success_url = reverse_lazy('property:add')


    def form_valid(self, form):
        cd = form.cleaned_data
        # TODO Currently making assumption only one item at a time.  Change to list
        prop = Property.objects.get_or_create_property(cd.get('mls'))

        return super(CreateProperty, self).form_valid(form)



class ListProperty(ListView):
    template_name = 'wish\list.html'

    def get_queryset(self):
        return Property.objects.filter(user=self.request.user)


class UpdateProperty(UpdateView):
    pass


class DeleteProperty(DeleteView):
    pass


class ViewProperty(DetailView):
    template_name = 'property\detail.html'

    model = Property

    pass



