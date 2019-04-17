from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^getContactsAPIView$',views.getContactsAPIView.as_view()),
    url(r'^getContactList$',views.ContactsListAPIView.as_view()),
    url(r'^getProductList$',views.ProductListAPIView.as_view()),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()