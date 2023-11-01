from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def quienesSomos(request):
    return render(request, 'quienes-somos.html', {})

def estatutos(request):
    return render(request, 'estatutos.html', {})

def miembros(request):
    return render(request, 'miembros.html', {})

def conferencias(request):
    return render(request, 'conferencias.html', {})

def cursillos(request):
    return render(request, 'cursillos.html', {})

def excursiones(request):
    return render(request, 'excursiones.html', {})

def colonias(request):
    return render(request, 'colonias.html', {})

def convivencias(request):
    return render(request, 'convivencias.html', {})

def talleres(request):
    return render(request, 'talleres.html', {})

def acompaniamientos(request):
    return render(request, 'acompaniamientos.html', {})

def pautas(request):
    return render(request, 'pautas.html', {})

def circular(request):
    return render(request, 'circular.html', {})

def carol(request):
    return render(request, 'carol.html', {})

def diabetesT1(request):
    return render(request, 'diabetes-t1.html', {})

def diabetesT2(request):
    return render(request, 'diabetes-t2.html', {})