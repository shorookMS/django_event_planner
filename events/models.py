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

	def __str__(self):
		return self.title

	


class BookedEvent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	ticket = models.PositiveIntegerField()

	def __str__(self):
		return self.event.title

	def are_tickets_overlimit(self):
		return self.ticket > self.event.seats

	def are_tickets_notvalid(self):
		return (self.ticket == 0)	

	def is_event_full(self):
		return self.event.seats == 0



