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
    p = []
    for palavra in palavras:
        x = [palavra, palavras.count(palavra)]
        p.append(x)
    contexto = {'qntd' : qntd, 'p' : p}
    return render(request, "contar.html", contexto)