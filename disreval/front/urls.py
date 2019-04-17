from django.conf.urls import url
from django.urls import include, path
from . import views
from django.views.generic import RedirectView
urlpatterns=[ 
    url(r'^$',views.welcome,name="Inicio"),
    url(r'^QuienesSomos$',views.whoAreWe,name="QuienesSomos"),
    url(r'^Clientes$',views.clients,name="Clientes"),
    url(r'^Ubicacion$',views.location,name="Ubicacion"),
    url(r'^Contactar$',views.getContacts,name="Contactar"),
    url(r'Productos',views.products,name="Productos"),
    url(r'^migrar$',views.product_upload, name="bd"),
]