from django.urls import path
from . import views
urlpatterns = [
    path('', views.to_do, name='to_do'),
    path('excluir_tarefa/<int:id>/', views.excluir_tarefa, name='excluir_tarefa')
]