from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView
) 
from rest_framework.response import Response
from django.db.models import Q
from .models import Contact, Role,Product,Department
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .serializer import ContactSerializer, ProductSerializer

from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination



class ContactsListAPIView(ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Contact.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(first_name__icontains=query)|
                Q(last_name__icontains=query)|
                Q(role__desc_role__icontains=query)
            ).distinct()
        return queryset_list


class getContactsAPIView(APIView):
    def get(self,request):
        contacts=Contact.objects.all()
        serializer=ContactSerializer(contacts,many=True)
        return Response(serializer.data)


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class=  PostPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Product.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)|
                Q(department__department_name__icontains=query)
            ).distinct()
        return queryset_list



