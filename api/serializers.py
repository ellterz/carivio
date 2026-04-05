from rest_framework import serializers
from cars.models import Car, Manufacturer, Category
from maintenance.models import MaintenanceRecord
from parts.models import Part

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)
    age = serializers.SerializerMethodField()
    total_maintenance_cost = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'name', 'manufacturer', 'category', 'year', 'vin', 'owner', 'age', 'total_maintenance_cost']

    def get_age(self, obj):
        return obj.age()

    def get_total_maintenance_cost(self, obj):
        return obj.total_maintenance_cost()

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField(read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MaintenanceRecord
        fields = ['id', 'car', 'date', 'description', 'cost', 'owner']

class PartSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Part
        fields = ['id', 'name', 'manufacturer', 'price', 'car', 'owner']
