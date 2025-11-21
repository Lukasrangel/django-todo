from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TaskForm
from .models import Task
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime
from .services import chamar_atencao

def mail(request):
    chamar_atencao()

@login_required()
def tasks(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')

    #dashboard
    ended = Task.objects.filter(done='done', user=request.user).count()
    todo = Task.objects.filter(done='doing', user=request.user).count()
    dateEnd = Task.objects.filter(done='done', user=request.user, updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user).order_by('priority')

        messages.info(request,  str(len(tasks)) + ' resultados encontrados para sua busca')
    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user).order_by('priority')
    else:
        task_list = Task.objects.all().order_by('priority').filter(user=request.user)

        paginator = Paginator(task_list, 14)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks':tasks, 'ended' : ended, 'todo' : todo, 'dateEnd' : dateEnd})


@login_required()
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form' : form})


@login_required() 
def viewTask(request, id):
    task = get_object_or_404(Task, pk=id)

    if task.user != request.user:
        return redirect('/')

    return render(request, 'tasks/task.html', {'task': task})


@login_required()
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)

    if task.user != request.user:
        return redirect('/')

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
    
    else:
            return render(request, 'tasks/editTask.html',{'form' : form, 'task' : task})


@login_required()
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)

    if task.user != request.user:
        return redirect('/')

    task.delete()

    messages.info(request, 'Tarefa deletada!')
    return redirect('/')


@login_required()
def changestatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if task.user != request.user:
        return redirect('/')

    if task.done == 'doing':
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()
    return redirect('/')



