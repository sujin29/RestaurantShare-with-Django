from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('index')
    return render(request, 'index.html')


def restaurantDetail(request):
    # return HttpResponse('restaurant detail')
    return render(request, 'restaurantDetail.html')

def restaurantCreate(request):
    # return HttpResponse('restaurant create')
    return render(request, 'restaurantCreate.html')

def categoryCreate(request):
    # return HttpResponse('category create')
    return render(request, 'categoryCreate.html')