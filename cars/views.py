from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cars.forms import CarForm, ManufacturerForm, CategoryForm
from cars.models import Car, Category, Manufacturer


class CarListView(ListView):
    model = Car
    template_name = 'cars/list.html'
    context_object_name = 'cars'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Cars'
        return context
class MyCarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'cars/my_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user).order_by('name')

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'{self.object.name} Details'
        context['is_owner'] = self.request.user.is_authenticated and self.object.owner == self.request.user
        return context

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/form.html'
    success_url = reverse_lazy('cars:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Car'
        return context

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/form.html'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy('cars:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"Edit {self.object.name}"
        context['car'] = self.object
        return context

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'common/confirm_delete.html'
    success_url = reverse_lazy('cars:list')
    context_object_name = 'object'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"Delete {self.object.name}"
        context['cancel_url'] = reverse_lazy('cars:detail', kwargs={'pk': self.object.pk})
        return context

class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'cars/manufacturer_form.html'
    success_url = reverse_lazy('cars:add')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Manufacturer'
        return context

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cars/category_form.html'
    success_url = reverse_lazy('cars:add')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Category'
        return context
