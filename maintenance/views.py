from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from maintenance.forms import MaintenanceForm
from maintenance.models import MaintenanceRecord


# Create your views here.
def maintenance_list(request: HttpRequest) -> HttpResponse:
    records = MaintenanceRecord.objects.all().order_by('-date')

    context = {
        'maintenance': records,
        'page_title': 'All Maintenance Records',
    }

    return render(request, 'maintenance/list.html', context)

def maintenance_detail(request: HttpRequest, pk: int) -> HttpResponse:
    record = get_object_or_404(MaintenanceRecord, pk=pk)

    context = {
        'maintenance': record,
        'page_title': f'Maintenance Detail: {record.car}'
    }
    return render(request, 'maintenance/detail.html', context)

def maintenance_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance:list')
    else:
        form = MaintenanceForm()

    context = {
        'form': form,
        'page_title': 'Add Maintenance Record',
    }

    return render(request, 'maintenance/add.html', context)

def maintenance_edit(request: HttpRequest, pk: int) -> HttpResponse:
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('maintenance:list')
    else:
        form = MaintenanceForm(instance=record)
    context = {
        'form': form,
        'page_title': 'Edit Maintenance Record',
    }

    return render(request, 'maintenance/edit.html', context)


def maintenance_delete(request: HttpRequest, pk: int) -> HttpResponse:
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('maintenance:list')
    context = {
        'maintenance': record,
        'page_title': 'Delete Maintenance Record',
    }

    return render(request, 'common/confirm_delete.html', context)