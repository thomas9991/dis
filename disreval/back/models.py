from django.db import models

# Create your models here.

class Role(models.Model):
    id_role=models.AutoField(primary_key=True)
    desc_role=models.CharField(max_length=30)

    def __str__(self):
        return self.desc_role

class Contact(models.Model):
    id_contact=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=30,null=True, blank=True)
    last_name=models.CharField(max_length=30,null=True,blank=True)
    email=models.EmailField(default=None)
    phone=models.BigIntegerField(default=None, blank=True,null=True)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.last_name)+' '+str(self.first_name)+' '+self.role.desc_role).upper()

class Category(models.Model):    
    id_category=models.AutoField(primary_key=True)
    category=models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Department(models.Model):
    department_id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=70)

    def __str__(self):
        return self.department_name

class Product(models.Model):
    bar_code=models.BigIntegerField(primary_key=True)
    plu=models.IntegerField(null=True)
    name=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    cost=models.IntegerField(null=True)    
    normal_price=models.IntegerField(null=True)
    m_com=models.FloatField(null=True)
    m_uti=models.FloatField(null=True)
    offer_price=models.IntegerField(null=True)
    stock=models.IntegerField(null=True)

    def getPrice(self):
        return "{:,}".format(self.normal_price).replace(',','.')
