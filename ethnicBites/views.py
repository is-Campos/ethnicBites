from django.shortcuts import render
from usuarios.decorators.clienteornone_required import clienteornone_required

@clienteornone_required()
def home(request):
    return render(request, 'ethnicBites/templates/index.html')