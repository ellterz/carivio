from django.urls import path

from cars.views import cars_list, car_detail, create_car, edit_car, delete_car

app_name = 'cars'

urlpatterns = [
    path('', cars_list, name='list'),
    path('<int:pk>/', car_detail, name='detail'),
    path('add/', create_car, name='add'),
    path('edit/',edit_car, name='edit'),
    path('delete/', delete_car, name='delete'),
]