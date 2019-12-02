"""desafio_jera Configuração das URL (URL Configuration)

    Neste arquivo são inseridas as configurações gerais e incluidas as rotas de cada aplicação, para que sejam mapeadas pelas views.
    (On this file are includes the general configurations and the routes of each app, to they be mapped by the views.)

    Para mais informações, acessar (For more information please see):
        https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('moviesplatform.urls')),
    path('accounts/', include('accounts.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]
