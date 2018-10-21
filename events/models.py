from django.db import models
from django.contrib.auth.models import User
class Event(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	description = models.TextField()
	location = models.CharField(max_length=150)
	date = models.DateField()
	time = models.TimeField()
	seats = models.PositiveIntegerField()

