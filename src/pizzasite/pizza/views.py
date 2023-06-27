from django.shortcuts import render, HttpResponse
from .models import Pizza, Deal

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets as viewset
from .serializers import PizzaSerializer

def index(request):
    context = {'pizzas' : Pizza.objects.all()}
    return render(request, "index.html", context)

class PizzaApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        # pizzas = Pizza.objects.filter(user = request.user.id)
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Pizza with given todo data
        '''
        data = {
            'pizza_name': request.data.get('pizza_name'), 
            'description': request.data.get('description'), 
            'price': request.data.get('price'),
            'deal': request.data.get('deal'),
            'user': request.user.id
        }
        serializer = PizzaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
