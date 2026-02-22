from django.urls import path

from cars.views import cars_list, car_detail, create_car, edit_car, delete_car, create_manufacturer, add_category

app_name = 'cars'

urlpatterns = [
    path('', cars_list, name='list'),
    path('<int:pk>/', car_detail, name='detail'),
    path('add/', create_car, name='add'),
    path('<int:pk>/edit/', edit_car, name='edit'),
    path('<int:pk>/delete/', delete_car, name='delete'),
    path('manufacturer/add/', create_manufacturer, name='manufacturer_add'),
    path('category/add', add_category, name='add_category'),
]