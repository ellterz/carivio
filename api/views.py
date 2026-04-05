from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from cars.models import Car
from maintenance.models import MaintenanceRecord
from parts.models import Part
from .serializers import CarSerializer, MaintenanceRecordSerializer, PartSerializer
from api.permissions import IsOwnerOrReadOnly

# Create your views here.


class CarListAPIView(ListAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Car.objects.all().select_related('manufacturer').prefetch_related('category').order_by('name')


class CarDetailAPIView(RetrieveAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Car.objects.all().select_related('manufacturer').prefetch_related('category')


class MaintenanceListAPIView(ListAPIView):
    serializer_class = MaintenanceRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MaintenanceRecord.objects.filter(owner=self.request.user).select_related('car')


class PartListAPIView(ListAPIView):
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Part.objects.filter(owner=self.request.user).prefetch_related('car')