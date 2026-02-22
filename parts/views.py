from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from parts.forms import PartForm
from parts.models import Part


# Create your views here.
def parts_list(request: HttpRequest) -> HttpResponse:
    parts = Part.objects.all()
    context = {
        'parts': parts,
        'page_title': 'All Parts'
    }

    return render(request, 'parts/list.html', context)

def part_detail(request:HttpRequest, pk:int) -> HttpResponse:
    part = get_object_or_404(Part, pk=pk)

    context = {
        'part': part,
        'page_title': 'Part Details'
    }

    return render(request, 'parts/detail.html', context)
def part_add(request: HttpRequest):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parts:list')
    else:
        form = PartForm()

    context = {
        'form': form,
        'page_title': 'Add Part'
    }

    return render(request, 'parts/form.html', context)

def part_edit(request: HttpRequest, pk:int) -> HttpResponse:
    part = get_object_or_404(Part, pk=pk)
    if request.method == 'POST':
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('parts:detail', pk=part.pk)
    else:
        form = PartForm(instance=part)
    context = {
        'form': form,
        'page_title': 'Edit Part'
    }

    return render(request, 'parts/form.html', context)

def part_delete(request: HttpRequest, pk:int) -> HttpResponse:
    part = get_object_or_404(Part, pk=pk)
    if request.method == 'POST':
        part.delete()
        return redirect('parts:list')
    context = {
        'object': part,
        'page_title': 'Delete Part'
    }
    return render(request, 'common/confirm_delete.html', context)