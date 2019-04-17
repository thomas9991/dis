from django.contrib import admin
from .models import Contact, Role, Category,Product

# Register your models here.
admin.site.register(Contact)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Product)