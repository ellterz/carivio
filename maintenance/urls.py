from django.urls import path
from maintenance.views import MaintenanceListView, MaintenanceDetailView, MaintenanceCreateView, MaintenanceUpdateView, MaintenanceDeleteView

app_name = 'maintenance'

urlpatterns = [
    path('', MaintenanceListView.as_view(), name='list'),
    path('<int:pk>/', MaintenanceDetailView.as_view(), name='detail'),
    path('add/', MaintenanceCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', MaintenanceUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', MaintenanceDeleteView.as_view(), name='delete'),
]
