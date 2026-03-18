from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista'),
    path('nova/', views.nova_tarefa, name='nova'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar'),
]