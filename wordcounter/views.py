from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    template_name = "home.html"
    return render(request, template_name)

def conta(request):
    texto = request.GET["fulltext"]
    print(texto)
    qntd = len(texto.split())
    palavras = texto.split()
    for palavra in palavras:
        print(palavras.count(palavra))
    contexto = {'qntd' : qntd, 'palavras' : palavras}
    return render(request, "contar.html", contexto)