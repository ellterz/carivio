from django.urls import path

from parts.views import parts_list, part_detail, part_add, part_edit, part_delete

app_name = 'parts'
urlpatterns = [
    path('', parts_list, name='list'),
    path('add/', part_add, name='add'),
    path('<int:pk>/', part_detail, name='detail'),
    path('<int:pk>/edit/', part_edit, name='edit'),
    path('<int:pk>/delete/', part_delete, name='delete'),
]