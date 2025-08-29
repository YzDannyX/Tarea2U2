from django.shortcuts import render
from .forms import EstudianteForm

def estudiante_form_view(request):
    form = EstudianteForm()
    return render(request, 'estudiantes/form.html', {'form': form})
