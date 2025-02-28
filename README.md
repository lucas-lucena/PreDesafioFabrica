# PreDesafioFabrica
Um compilado de todos os conhecimentos adiquiridos no workshop da Fabrica de Software.

## Git e Github
Primeiro eu configurei uma chave SSH na minha máquina para me comunicar com a minha conta do github.
Segui o passo a passo descrito em [hello-git](https://github.com/lucas-lucena/hello-git)

Criei o repositório remoto no Github com README.md e .gitignore (Python)

Clonei o repositório remoto para minha máquina via a chave SSH configurada previamente

    $ git clone "link para a chave ssh"

## Ambiente virtual

Com o repositório clonado, eu criei meu ambiente virtual

    $ cd ~/caminho/para/repositorio/local/
    $ python -m venv venv

Ativando ambiente virtual

    $ source ./venv/bin/activate

*Caso queira desativar o ambiente virtual:*

    (venv) $ deactivate

## Requisitos 

Agora instalando as bibliotecas necessárias e criando o arquivo `requirements.txt`

    (venv) $ pip install django
    (venv) $ pip install djangorestframework
    (venv) $ pip freeze >> requirements.txt
    
## Configurações iniciais do Django

Agora vamos iniciar o projeto

    (venv) $ django-admin startproject project .
    

Vamos rodar o server

    (venv) $ python manage.py runserver

Se a instalação for bem sucedida ele nos mostrará uma página em http://127.0.0.1:8000

Agora vamos iniciar o app

    (venv) $ python manage.py startapp app

Com o project e o app criados, a primeira coisa que queremos fazer é registrar **app** e o **restframework** em `INSTALLED_APPS` dentro de `settings.py`

```py
INSTALLED_APPS = [
    ...,
    'app',
    'rest_framework',
]
```

Podemos também fazer alterações no campo de Internationalization em `settings.py`

Eu mudei a lingua de en-us para pt-br

```py
LANGUAGE_CODE = 'pt-br'
```

## Criando nossa primeira view

Vamos criar a primeira view simples em `app/views.py`

    (venv) $ cd ./app
    (venv) $ nano views.py  # Use o editor de sua preferência, para os exemplos irei usar o nano

```py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")
```

Dentro de `./app` vamos criar o arquivo de rotas`urls.py` 

    (venv) $ touch urls.py
    (venv) $ nano urls.py
    
```py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home, name='home'),
]
```

Vamos conectar as rotas criadas ao arquivo `urls.py` dentro de `/project`

    (venv) $ cd ../project
    (venv) $ nano urls.py

```py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app', include('app.urls')),
]

```
