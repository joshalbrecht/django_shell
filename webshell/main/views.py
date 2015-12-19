from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Basic index page")

def model(request):
    from main.models import AWSTestModel
    m = AWSTestModel.objects.all()[0]
    return HttpResponse("We have a model with text: " + m.random_text)

def newmodel(request):
    from main.models import AWSTestModel
    m = AWSTestModel.objects.all()[0]
    return HttpResponse("Model got a new field: " + m.new_field)
