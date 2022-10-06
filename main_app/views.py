# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Car, Engine, Tire
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
#...
from django.views.generic.base import TemplateView
from django.urls import reverse
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
#...
class About(TemplateView):
    template_name = "about.html"


@method_decorator(login_required, name='dispatch')
class CarList(TemplateView):
    template_name = "car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        make = self.request.GET.get("make")
        
        print(make)
        if make != None:
            context["cars"] = Car.objects.filter(
                make__icontains=make, user=self.request.user)
            context["header"] = f"Searching for {make}"
        else:
            context["cars"] = Car.objects.filter(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'img', 'trim', 'price']
    template_name = "car_create.html"
    success_url = "/cars/"

    # This is our new method that will add the user into our submitted form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CarCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class CarDetail(DetailView):
    model = Car
    template_name = "car_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["tires"] = Tire.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'img', 'trim', 'price']
    template_name = "car_update.html"
    success_url = "/cars/"



@method_decorator(login_required, name='dispatch')
class CarDelete(DeleteView):
    model = Car
    template_name = "car_delete_confirmation.html"
    success_url = '/cars/'


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class TireCarAssoc(View):
    def get(self, request, pk, car_pk):
        assoc = request.GET.get("assoc")
        print(assoc)
        if assoc == "remove":
            print(pk)
            print(car_pk)

            Tire.objects.get(pk=pk).cars.remove(car_pk)
        if assoc == "add":
            Tire.objects.get(pk=pk).cars.add(car_pk)
        return redirect('home')


class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
