from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from parts.forms import PartForm
from parts.models import Part


class PartListView(LoginRequiredMixin, ListView):
    model = Part
    template_name = 'parts/list.html'
    context_object_name = 'parts'

    def get_queryset(self):
        return Part.objects.filter(owner=self.request.user).prefetch_related('car').order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Parts'
        return context

class PartDetailView(LoginRequiredMixin, DetailView):
    model = Part
    template_name = 'parts/detail.html'
    context_object_name = 'part'


    def get_queryset(self):
        return Part.objects.filter(owner=self.request.user).prefetch_related('car')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Part Details'
        return context

class PartCreateView(LoginRequiredMixin, CreateView):
    model = Part
    form_class = PartForm
    template_name = 'parts/form.html'
    success_url = reverse_lazy('parts:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Part'
        return context

class PartUpdateView(LoginRequiredMixin, UpdateView):
    model = Part
    form_class = PartForm
    template_name = 'parts/form.html'

    def get_queryset(self):
        return Part.objects.filter(owner=self.request.user).prefetch_related('car')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('parts:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Edit Part'
        return context


class PartDeleteView(LoginRequiredMixin, DeleteView):
    model = Part
    template_name = 'common/confirm_delete.html'
    success_url = reverse_lazy('parts:list')
    context_object_name = 'object'

    def get_queryset(self):
        return Part.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Part'
        context['cancel_url'] = reverse_lazy('parts:detail', kwargs={'pk': self.object.pk})
        return context