from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail),
    path('restaurantCreate/', views.restaurantCreate),
    path('categoryCreate/', views.categoryCreate),
]