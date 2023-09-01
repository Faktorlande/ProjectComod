from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse


from .models import Workers
from .forms import TableWorkersForm

def workers(request):
    form_table = TableWorkersForm()
    raws_workers = Workers.objects.all()
    context = {
        'form_table': form_table,
        'title': 'Таблица сотрудников',
        'table': raws_workers,
        'form': form_table,
    }
    return render(request, 'workers/table_workers.html', context=context)