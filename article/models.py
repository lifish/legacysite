from django.db import models

# Create your models here.
class Article(models.Model):
	ARTICLE_TYPE = (
		('LE','lecturer'),
		('ST','student'),
		('AC','achievement'),
	)
	subject = models.CharField(max_length=200)	
	name = models.CharField(max_length=200)
	author = models.CharField(blank=True, max_length=200)
	company = models.CharField(blank=True, max_length=200)
	title = models.CharField(blank=True, max_length=200)
	content = models.TextField()
	group = models.CharField(max_length=2, choices=ARTICLE_TYPE)
