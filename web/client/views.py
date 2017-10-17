from django.shortcuts import render
from django.http import Http404

# Create your views here.

def task_detail(request, id):
    return render(request, "task.html", {"task": id})
