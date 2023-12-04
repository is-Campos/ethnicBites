from django.shortcuts import render

def home(request):
    return render(request, 'ethnicBites/templates/index.html')