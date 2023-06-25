from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Writer(models.Model):
	name = models.CharField(max_length = 100)
	bio = models.TextField()
	pic = models.FileField(upload_to = "writer/")

	def __str__(self):
		return self.name

class Book(models.Model):
	writer = models.ForeignKey(Writer, on_delete = models.CASCADE)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	stock = models.IntegerField()
	coverpage = models.FileField(upload_to = "coverpage/")
	description = models.TextField()

	def __str__(self):
	    return self.name