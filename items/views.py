from django.shortcuts import render, redirect
from .models import *


def tasks(request):
    if request.method == "POST":
        data = request.POST
        task_name = data.get('task_name')
        items.objects.create(
            task_name=task_name
        )
        return redirect('/')

    QuerySet = items.objects.all()
    Context = {
        'data': QuerySet
    }
    return render(request, 'index.html', Context)


def delete_task(request, name):
    name = items.objects.filter(name)
    print(name)
    return redirect("/")
