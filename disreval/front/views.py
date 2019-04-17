from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Contact
from back.models import Product, Department

import csv, io
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html")

def welcome(request):
    return render(request,"inicio.html")

def whoAreWe(request):
    return render(request,'quienes_somos.html')

def location(request):
    return render(request,'ubicacion.html')

def clients(request):
    return render(request,'clientes.html')

def products(request):
    product_list=Product.objects.order_by('offer_price')
    department_list=Department.objects.all().distinct()
    queryset_list = Product.objects.all()
    query = request.GET.get("q")
    if query:

        queryset_list = queryset_list.filter(
            Q(name__icontains=query)|
            Q(department__department_name__icontains=query)
        ).distinct().order_by('normal_price')
      


    print(query)
    page=request.GET.get('page', 1)
    paginator = Paginator(queryset_list, 20)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'productos.html', { 'products': products,'department_list':department_list,'query':query})
  



def getContacts(request):
    contact_list=Contact.objects.order_by('role')
    page = request.GET.get('page', 1)

    paginator = Paginator(contact_list, 2)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'contactos.html', { 'contacts': contacts })

def product_upload(request):
    template="migrar.html"
    prompt ={
        'order':'order of the CSV should be first_name, last_name'
    }
    if request.method =="GET":
        return render(request,'migrar.html')

    csv_file=request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')

    data_set=csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    c=0
    u=0
    for column in csv.reader(io_string,delimiter=';',  quotechar="|"):
        if Department.objects.filter(department_name=column[3]).exists():

            
            print('Existe')
        else:
            regDB=Department.objects.create(
                department_name=column[3]
                )
            

        

    

        if Product.objects.filter(bar_code=column[1]).exists():
            u=u+1
            dep=Department.objects.get(department_name=column[3])
            Product.objects.filter(bar_code=column[1]).update(
                plu=column[0],
                name=column[2],
                department=dep,
                cost=column[4],
                normal_price=column[5],
                m_com=float(column[6].replace(',','.')),
                m_uti=float(column[7].replace(',','.')),
                offer_price=int(column[8].replace('.','')),
                stock=int(column[9].replace('.',''))
                


                )
            
        else:
            dep=Department.objects.get(department_name=column[3])           
            regDB=Product.objects.create(
                bar_code=column[1],
                plu=column[0],
                name=column[2],
                department=dep,
                cost=column[4],
                normal_price=column[5],
                m_com=float(column[6].replace(',','.')),
                m_uti=float(column[7].replace(',','.')),
                offer_price=int(column[8].replace('.','')),
                stock=int(column[9].replace('.',''))
                )
            
            c=c+1

            print(c)
            
           
            

    print('Creados:'+str(c)+' Actualizados:'+str(u))
        
        
    context ={}
    return render(request,template,context)