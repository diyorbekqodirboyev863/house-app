from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='add/', view=views.add, name='add'),
    path(route='details/<int:id>', view=views.details, name='details'),
]