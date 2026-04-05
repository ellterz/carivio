from django.urls import path
from api.views import CarListAPIView, CarDetailAPIView, MaintenanceListAPIView, PartListAPIView

app_name = 'api'

urlpatterns = [
    path('cars/', CarListAPIView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail'),
    path('maintenance/', MaintenanceListAPIView.as_view(), name='maintenance-list'),
    path('parts/', PartListAPIView.as_view(), name='parts-list'),
]