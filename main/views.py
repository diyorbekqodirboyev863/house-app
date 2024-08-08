from django.shortcuts import render

# Home.
def home(request):
    return render(request=request, template_name='home.html', context={})