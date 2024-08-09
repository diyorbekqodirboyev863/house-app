from django.shortcuts import render, redirect
from django.contrib import messages as msg
from .models import House, Category
from .forms import HouseForm

# Home.
def home(request):
    houses = House.objects.all()
    categories = Category.objects.all()
    return render(request=request, template_name='home.html', context={'houses': houses, 'categories': categories})

# Add house.
def add_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg.success(request=request, message='House added successfully.')
            return redirect(to='home')
        else:
            msg.warning(request=request,
                message='Failed to add house. Please make sure all required fields are filled correctly.')
    else:
        form = HouseForm()
    return render(request=request, template_name='add_house.html', context={'form': form})