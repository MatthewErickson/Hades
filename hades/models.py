from __future__ import unicode_literals

from django import forms
from django.db import models
from django.forms import ModelForm
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=64, default="")
	content = models.TextField()
	post_date = models.DateTimeField('date published', default=timezone.now())

	def __str__(self):
		return self.title

class Show(models.Model):
	name = models.CharField(max_length=64, default="")

	def __str__(self):
		return self.name

class Episode(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	name = models.CharField(max_length=64, default="")
	season = models.IntegerField(default=0)
	number = models.IntegerField(default=0)

	def __str__(self):
		return self.name
		#return "S%d-E%d: %s" % (self.season, self.number, self.name)
