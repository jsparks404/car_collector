from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('cars/', views.CarList.as_view(), name="car_list"),
    path('cars/new/', views.CarCreate.as_view(), name="car_create"),
    path('cars/<int:pk>/', views.CarDetail.as_view(), name="car_detail"),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name="car_update"),
    path('cars/<int:pk>/delete', views.CarDelete.as_view(), name="car_delete"),
    path('cars/<int:pk>/engine/new', views.EngineCreate.as_view(), name="engine_create"),
    path('tires/<int:pk>/cars/<int:song_pk>/', views.TireCarAssoc.as_view(), name="tire_car_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]


