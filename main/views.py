from django.shortcuts import render
from .models import House

# Home.
def home(request):
    houses = House.objects.all()
    return render(request=request, template_name='home.html', context={'houses': houses})