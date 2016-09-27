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

class LoginForm(forms.Form):
	email = forms.CharField(
		max_length=64,
		label='',
		widget=forms.TextInput(
			attrs={
				'type': 'email',
				'placeholder': 'Email',
				'autocomplete': 'off',
				'class': 'form-control',
			}
		)
	)

	password = forms.CharField(
		max_length=64,
		label='',
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'autocomplete': 'off',
				'class': 'form-control',
			}
		)
	)

class SignUpForm(forms.Form):
	first_name = forms.CharField(
		max_length=64,
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder': 'First Name',
				'autocomplete': 'off',
				'class': 'form-control',
			}
		)
	)

	last_name = forms.CharField(
		max_length=64,
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Last Name',
				'autocomplete': 'off',
				'class': 'form-control',
			}
		)
	)
	
	email = forms.CharField(
		max_length=64,
		label='',
		widget=forms.TextInput(
			attrs={
				'type': 'email',
				'placeholder': 'Email',
				'autocomplete': 'off',
				'class': 'form-control',
			}
		)
	)

	password = forms.CharField(
		max_length=64,
		label='',
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'autocomplete': 'off',
				'class': 'form-control',
			}
		)
	)
