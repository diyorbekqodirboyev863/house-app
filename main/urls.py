from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='add/', view=views.add_house, name='add')
]