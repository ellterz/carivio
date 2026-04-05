from django.urls import path
from cars.views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, ManufacturerCreateView, \
    CategoryCreateView, MyCarListView

app_name = 'cars'

urlpatterns = [
    path('', CarListView.as_view(), name='list'),
    path('my/', MyCarListView.as_view(), name='my_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='detail'),
    path('add/', CarCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='delete'),
    path('manufacturer/add/', ManufacturerCreateView.as_view(), name='manufacturer_add'),
    path('category/add/', CategoryCreateView.as_view(), name='add_category'),
]