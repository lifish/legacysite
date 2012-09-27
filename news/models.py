from django.db import models

# Create your models here.
class News(models.Model):
	subject = modles.CharField(max_length=200)
	date = modles.DateTimeField(auto_now_add=True)
	content = modles.TextField()
