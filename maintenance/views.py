from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from maintenance.forms import MaintenanceForm
from maintenance.models import MaintenanceRecord


class MaintenanceListView(LoginRequiredMixin, ListView):
    model = MaintenanceRecord
    template_name = 'maintenance/list.html'
    context_object_name = 'maintenance'

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(owner=self.request.user).select_related('car').order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Maintenance Records'
        return context

class MaintenanceDetailView(LoginRequiredMixin, DetailView):
    model = MaintenanceRecord
    template_name = 'maintenance/detail.html'
    context_object_name = 'record'

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(owner=self.request.user).select_related('car')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Maintenance Detail: {self.object.car}'
        return context


class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    model = MaintenanceRecord
    form_class = MaintenanceForm
    template_name = 'maintenance/add.html'
    success_url = reverse_lazy('maintenance:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        car_pk = self.request.GET.get('car')
        if car_pk:
            initial['car'] = car_pk
        return initial

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Maintenance Record'
        return context
class MaintenanceUpdateView(LoginRequiredMixin, UpdateView):
    model = MaintenanceRecord
    form_class = MaintenanceForm
    template_name = 'maintenance/edit.html'

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(owner=self.request.user).select_related('car')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('maintenance:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = self.object
        context['page_title'] = 'Edit Maintenance Record'
        return context
class MaintenanceDeleteView(LoginRequiredMixin, DeleteView):
    model = MaintenanceRecord
    template_name = 'common/confirm_delete.html'
    success_url = reverse_lazy('maintenance:list')
    context_object_name = 'object'

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(owner=self.request.user).select_related('car')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Maintenance Record'
        context['cancel_url'] = reverse_lazy('maintenance:detail', kwargs={'pk': self.object.pk})
        return context