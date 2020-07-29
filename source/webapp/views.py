from webapp.models import Task
from django.shortcuts import redirect, get_object_or_404, render
from webapp.forms import TaskForm


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'add.html', {'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(description=form.cleaned_data['description'], status=form.cleaned_data['status'],
                                       detailed_desc=form.cleaned_data['detailed_desc'],
                                       finish_date=form.cleaned_data['finish_date'])
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'add.html', {'form': form})


def delete_view(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect(index_view)
    return render(request, "delete_view.html", {'task': task})


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={
            'description': task.description,
            'detailed_desc': task.detailed_desc,
            'status': task.status,
            'finish_date': task.finish_date,
        })
        return render(request, 'update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.detailed_desc = form.cleaned_data['detailed_desc']
            task.status = form.cleaned_data['status']
            task.finish_date = form.cleaned_data['finish_date']
            task.save()
            return redirect(task_view, pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})


def admin_delete_view(request):
    tasks = Task.objects.all()
    if request.method == 'GET':
        return render(request, 'admin_delete.html', {'tasks': tasks})
    elif request.method == 'POST':
        selected_tasks = request.POST.getlist('pk')
        for pk in selected_tasks:
            task = get_object_or_404(Task, id=pk)
            task.delete()
        return redirect('index')