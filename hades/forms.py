from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class BlogForm(forms.Form):
	title = forms.CharField(
		max_length=64,
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Title',
				'autocomplete': 'off',
				'class': 'form-control',
			}
		)
	)
	content = forms.CharField(
		label='',
		max_length=1024,
		widget=forms.Textarea(
			attrs={
				'placeholder': 'Write your content here...',
				'class': 'form-control',
			}
		)
	)
