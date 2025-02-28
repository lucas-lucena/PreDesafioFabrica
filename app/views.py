from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')


### Codigo criado apenas para exibir mensagem inicial em no navegador
# from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("Hello World")