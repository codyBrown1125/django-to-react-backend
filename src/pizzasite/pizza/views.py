from django.shortcuts import render, HttpResponse
from .models import Pizza, Deal

from rest_framework import viewsets as viewset
from .serializers import PizzaSerializer

def index(request):
    context = {'pizzas' : Pizza.objects.all()}
    return render(request, "index.html", context)

def PizzaView(viewset.ModelViewSets)
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()