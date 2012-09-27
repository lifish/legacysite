from django.db import models

# Create your models here.
class News(models.Model):
	subject = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
