from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

from .models import Wish
from .forms import CreateWishFrom

class CreateWish(CreateView):
    template_name = 'wish\create.html'
    model = Wish
    form_class = CreateWishFrom
    success_url = reverse_lazy('wish:add')


    def form_valid(self, form):
        wish = form.save(commit=False)
        wish.user = self.request.user
        wish.save()
        return super(CreateWish, self).form_valid(form)



class ListWish(ListView):
    template_name = 'wish\list.html'

    def get_queryset(self):
        return Wish.objects.filter(user=self.request.user)


class UpdateWish(UpdateView):
    pass


class DeleteWish(DeleteView):
    pass


class ViewWish(DetailView):
    pass



