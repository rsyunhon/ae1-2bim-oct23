"""
    Manejo de urls para la aplicación
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views
from django.views.generic import TemplateView


urlpatterns = [
        path('', TemplateView.as_view(template_name='listadoOpciones.html'), name='listadoOpciones'),
        path('listarPaises', views.listarPaises, name='listarPaises'),
        path('listarBarrios', views.listarBarrios, name='listarBarrios'),
 ]