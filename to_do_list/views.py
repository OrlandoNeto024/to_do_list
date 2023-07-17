from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
# Create your views here.
def to_do(request):
    tarefas = Tasks.objects.all()
    if request.method == 'GET':
        return render(request, 'to_do.html', {'tarefas': tarefas})
    else:
        task = request.POST.get('tarefa')
        tarefa = Tasks(tarefa=task)
        tarefa.save()
        return redirect('to_do')

def excluir_tarefa(request, id):
    tarefa_deletar = Tasks.objects.get(id=id)
    tarefa_deletar.delete()
    return redirect('to_do')