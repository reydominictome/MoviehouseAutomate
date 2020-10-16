from django.db import models
from datetime import datetime

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  
    street = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    birth_date = models.DateField(default = datetime.now())
    gender = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    spouse_name = models.CharField(max_length=50, blank=True)
    spouse_occupation = models.CharField(max_length=50, blank=True)
    no_of_children = models.IntegerField()

    class Meta:
        db_table='Person'
    
class Customer(Person):
    date_registered = models.DateField(default = datetime.now())
    profile_picture = models.ImageField(upload_to='profile_picture', null=True, blank=True, default='profile_picture/default.png')
    is_deleted= models.BooleanField(default=False)

    class Meta:
        db_table='Customer'
    
