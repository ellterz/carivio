from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


from cars.forms import CarForm
from cars.models import Car


# Create your views here.
def cars_list(request: HttpRequest) -> HttpResponse:
    cars = Car.objects.all()

    context = {
        'cars': cars,
        'page_title': 'all_cars'
    }

    return render(request, 'cars/list.html', context)

def car_detail(request: HttpRequest, pk: int) -> HttpResponse:
    car = get_object_or_404(Car, pk=pk)

    context = {
        'car': car,
        'page_title': 'car_detail',
    }

    return render(request, 'cars/detail.html', context)


def create_car(request: HttpRequest):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars:list')
    else:
        form = CarForm()

    context = {
        'form': form,
        'page_title': 'Add Car',
    }
    return render(request, 'cars/form.html', context)


def edit_car(request: HttpRequest, pk: int) -> HttpResponse:
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars:detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    context = {
        'form': form,
        'car': car,
        'page_title': f"Edit {car.name}",
    }

    return render(request, 'cars:form.html', context)

def delete_car(request: HttpRequest, pk: int) -> HttpResponse:
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('cars:list')
    context = {
        'car': car,
        'page_title': f"Delete {car.name}",
    }

    return render(request,'common/confirm_delete.html', context)