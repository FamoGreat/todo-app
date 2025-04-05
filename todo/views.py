from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def addTask(request):
    if request.method == 'POST':
        task = request.POST['task']
        if task:
            Task.objects.create(task=task)
            return redirect('home')
        else:
            return render(request, 'home.html', {'error': 'Task cannot be empty'})
    return render(request, 'home.html')


def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task_name = request.POST['task']
        if task_name:
            task.task = task_name
            task.save()
            return redirect('home')
        else:
            return render(request, 'edit_task.html', {'task': task, 'error': 'Task cannot be empty'})
    return render(request, 'edit_task.html', {'task': task})


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


def completeTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def markAsIncomplete(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')