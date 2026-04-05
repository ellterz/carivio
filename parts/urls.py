from django.urls import path
from parts.views import PartListView, PartDetailView, PartCreateView, PartUpdateView, PartDeleteView

app_name = 'parts'

urlpatterns = [
    path('', PartListView.as_view(), name='list'),
    path('<int:pk>/', PartDetailView.as_view(), name='detail'),
    path('add/', PartCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', PartUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PartDeleteView.as_view(), name='delete'),
]