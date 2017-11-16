"""parqueadero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from parkapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tipos/list', views.list_tipos, name='list_tipos'),
    url(r'^tipos/update/(?P<tipoid>\d+)', views.update_tipo, name='update_tipo'), #formulario para editar
    url(r'^usuarios/add', views.add_usuario, name='add_usuario'),
    url(r'^usuarios/list', views.list_usuarios, name='list_usuarios'),
    url(r'^usuarios/update/(?P<usuarioid>\d+)', views.update_usuario, name='update_usuario'), #formulario para editar
    url(r'^usuarios/delete/(?P<usuarioid>\d+)', views.delete_usuario, name='delete_usuario'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^ticket/add', views.tickets, name='add_ticket'),
    url(r'^ticket/calcular/(?P<ticketid>\d+)', views.calcular, name='calcular'),
    url(r'^ticket/confirmar/', views.confirmar, name='confirmar'),
]
