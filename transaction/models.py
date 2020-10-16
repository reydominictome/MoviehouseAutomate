from django.db import models
from datetime import datetime
from movie.models import Movie
from customer.models import Customer
# Create your models here.

class Transaction(models.Model):
    customer_id = models.ForeignKey(Customer, null = False, blank = False, on_delete = models.CASCADE, related_name = "Customer")
    movie_id = models.ManyToManyField(Movie, null = False, blank = False, related_name = "Movie")
    cost = models.FloatField()
    date_of_transaction = models.DateField(default = datetime.now())
    room_no = models.IntegerField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table="Transaction"
