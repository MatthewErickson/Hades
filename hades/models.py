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

class PageView(models.Model):
    page_name = models.CharField(max_length=32, default="")
    page_count = models.BigIntegerField()
