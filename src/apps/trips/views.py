from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

from src.apps.property.models import Property


from .models import ClientsTrip, PropertyOnTrip, Trip
from .forms import CreateTripForm

import logging


class CreateTrip(CreateView):
    template_name = 'trips/create.html'
    form_class = CreateTripForm

    def get_context_data(self, **kwargs):
        context = super(CreateTrip, self).get_context_data(**kwargs)
        context['objects'] = Trip.objects.filter(agent=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        property_list = request.POST.getlist('property')

        if property_list:
            new_list = []

            for place in property_list:
                p, is_object = Property.objects.loaded_or_create(place)

                if is_object:
                    new_list.append(p.pk)
                else:
                    new_list.append(p)

            request.POST = request.POST.copy()
            request.POST.setlist('property', new_list)

        return super(CreateTrip, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        cd = form.cleaned_data

        trip = form.save(commit=False)
        trip.agent = self.request.user
        trip.save()

        # As both items have a Through table, we need to deal with them each
        for c in cd.get('clients'):
            ClientsTrip.objects.create(trip=trip, clients=c)
        for p in cd.get('property'):
            PropertyOnTrip.objects.create(trip=trip, property=p)

        return HttpResponseRedirect(reverse_lazy('trips:view'))

class ViewAll(ListView):
    model = Trip
    template_name = 'trips/list.html'


    def get_queryset(self):
        return Trip.objects.filter(agent=self.request.user)


class ViewTrip(DetailView):
    model = Trip
    template_name = 'trips/detail.html'


class UpdateTrip(UpdateView):
    model = Trip
    template_name = 'trips/create.html'

class DeleteTrip(DeleteView):
    pass



