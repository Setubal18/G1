from .models import *
from django.shortcuts import render, get_object_or_404
# Create your views here.

def chamada(request):
    chamada = Chamada.objects.all()
    chamadas = {'lista': chamada}
    return render(request,'home.html', chamadas)

def chamada_list(request, pk):
    chamada= get_object_or_404(Chamada,pk=pk)
    return render(request,'post.html', {'chamada':chamada})