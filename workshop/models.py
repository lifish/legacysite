from django.db import models

# Create your models here.
class Workshop(models.Model):
	WORKSHOP_TYPE = (
		('ST','step'),
		('CO','core'),
	)
	group = models.CharField(max_length=2, choices=WORKSHOP_TYPE)
	name = models.CharField(max_length=200)
	content = models.TextField()
