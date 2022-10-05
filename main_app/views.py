from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Car, Engine, Tire
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
#...
from django.views.generic.base import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tires"] = Tire.objects.all()
        return context
#...
#...
class About(TemplateView):
    template_name = "about.html"


class CarList(TemplateView):
    template_name = "car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        make = self.request.GET.get("make")
        
        print(make)
        if make != None:
            context["cars"] = Car.objects.filter(make__icontains=make) 
        else:
            context["cars"] = Car.objects.all()
        return context


class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'img', 'trim', 'price']
    template_name = "car_create.html"
    success_url = "/cars/"


class CarDetail(DetailView):
    model = Car
    template_name = "car_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tires"] = Tire.objects.all()
        return context

class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'img', 'trim', 'price']
    template_name = "car_update.html"
    success_url = "/cars/"


class CarDelete(DeleteView):
    model = Car
    template_name = "car_delete_confirmation.html"
    success_url = '/cars/'


class EngineCreate(View):
    def post(self, request, pk):
        designation = request.POST.get('designation')
        displacement = request.POST.get('displacement')
        induction = request.POST.get('induction')
        configuration = request.POST.get('configuration')
        horsepower = request.POST.get('horsepower')
        torque = request.POST.get('torque')
        car = Car.objects.get(pk=pk)
        Engine.objects.create(designation=designation, displacement=displacement, induction=induction, configuration=configuration, horsepower=horsepower, torque=torque, car=car)
        return redirect('car_detail', pk=pk)


class TireCarAssoc(View):
    def post(self, request, pk, car_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Tire.objecs.get(pk=pk).songs.remove(song_pk)
        if assoc == "add":
            Tire.objects.get(pk=pk).songs.add(car_pk)
        return redirect('home')