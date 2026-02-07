from django.urls import path

from maintenance.views import maintenance_list, maintenance_detail, maintenance_create, maintenance_edit, \
    maintenance_delete

app_name = 'maintenance'

urlpatterns = [
    path('', maintenance_list, name='list'),
    path('<int:pk>/', maintenance_detail, name='detail'),
    path('add/', maintenance_create, name='add'),
    path('<int:pk>/edit/', maintenance_edit, name='edit'),
    path('<int:pk>/delete/', maintenance_delete, name='delete'),

]
