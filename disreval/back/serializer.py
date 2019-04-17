from rest_framework import serializers
from .models import Role, Contact, Category, Product, Department
from rest_framework.serializers import (
    EmailField,
    CharField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    ReadOnlyField
)

class ContactSerializer(ModelSerializer):
    role = ReadOnlyField(source='role.desc_role')

    class Meta:
        model = Contact
        fields=[
            'first_name',
            'last_name',
            'email',
            'phone',
            'role',
            
        ]

class ProductSerializer(ModelSerializer):
    department = ReadOnlyField(source='department.department_name')

    class Meta:
        model = Product
        fields=[
            'bar_code',
            'plu',
            'name',
            'department',
            'cost',
            'normal_price',
            'm_com',
            'm_uti',
            'offer_price',
            'stock'
            
        ]

