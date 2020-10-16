from django.db import models
from datetime import datetime

class Movie(models.Model):
	sku = models.CharField(max_length=50)
	date_registered = models.DateField(default = datetime.now())
	genre = models.TextField()
	title = models.CharField(max_length=100)
	release_date = models.DateField(default = datetime.now())
	director = models.CharField(max_length=100)
	casts = models.TextField()
	price = models.FloatField()
	no_of_items = models.IntegerField()
	image = models.ImageField(upload_to='cover_image', null=True, blank=True, default='cover_image/default.png')
	is_deleted = models.BooleanField(default=False)

	class Meta:
		db_table="Movie"