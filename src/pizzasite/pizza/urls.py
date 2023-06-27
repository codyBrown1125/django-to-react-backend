from django.urls import path

from . import views
from .views import PizzaApiView

urlpatterns = [
    path("", views.index, name="index"),
     path('api', PizzaApiView.as_view()),
]

