from django.db import models

# Create your models here.
class Contact(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,blank=True, default=None)
    last_name=models.CharField(max_length=30,blank=True, default=None)
    role=models.CharField(max_length=30,blank=True)
    phone=models.CharField(max_length=30,blank=True, default=None)
    email=models.EmailField(blank=True)


    def __str__(self):
        return self.name
	