# Django imports #
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Model imports #
from .models import Blog, Show, Episode
from .forms import BlogForm, LoginForm, SignUpForm

# Misc. imports #
import datetime, time

pageSize = 5

# View functions #
def index(request):
	return render(request, 'hades/index.html')

def signup(request):
	if request.method == 'POST':
		signUpForm = SignUpForm(request.POST)
		if signUpForm.is_valid():
			try:
				first_name = request.POST['first_name']
				last_name = request.POST['last_name']
				email = request.POST['email']
				password = request.POST['password']
			except(KeyError):
				messages.warning(request, 'Unknown parameter error. Please contact support')
				return redirect('hades:signup')

			try:
				user = User.objects.create_user(email, email, password)
				user.first_name = first_name
				user.last_name = last_name
				user.save()
				submitBlog("Account created", "Welcome, " + first_name + " " + last_name)
				login(request, user)
				messages.success(request, 'Account created. Login successful')
				return redirect('hades:index')
			except:
				# user already exists #
				messages.error(request, 'Account creation failed.')
				messages.error(request, 'That email (%s) is already registered.' % email)
				return redirect('hades:signup')
	else:
		signUpForm = SignUpForm()

	return render(request, 'hades/signup.html', {
		'signUpForm': signUpForm,
	})

def doLogin(request):
	if request.method == 'POST':
		loginForm = LoginForm(request.POST)
		if loginForm.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(username=email, password=password)
			if user is not None:
				login(request, user)
				return redirect('hades:index')
			else:
				messages.error(request, 'Login failed. Invalid email and/or password')
				return redirect('hades:login')
	else:
		loginForm = LoginForm()
		
	return render(request, 'hades/login.html', {
		'loginForm': loginForm
	})

def doLogout(request):
	logout(request)
	messages.success(request, "You've successfully logged out. Thank you. Please come again.")
	return redirect('hades:index')

@login_required
def blog(request, page=-1):
	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			submitBlogFromRequest(request)
			return redirect('hades:blog')
	else:
		form = BlogForm()
	
	allBlogs = Blog.objects.order_by('-post_date')
	length = len(allBlogs)
	if length == 0:
		lastPage = 0
	else:
		lastPage = (length -1) // pageSize
	
	if page == -1:
		page = lastPage

	startIndex = int(page) * pageSize
	endIndex = startIndex + pageSize

	blogs = Blog.objects.order_by('post_date')[startIndex:endIndex]
	return render(request, 'hades/blog.html', {
		'blogs' : blogs,
		'form' : form,
		'page' : page,
		'lastPage': lastPage,
	})

def submitBlogFromRequest(request):
	try:
		title = request.POST['title']
		content = request.POST['content']
	except(KeyError):
		pass
	else:
		submitBlog(title, content)

def submitBlog(title, content):
	post_date = timezone.now()
	blog = Blog(title=title, content=content, post_date=post_date)
	blog.save()

@login_required
def video(request, showName=""):
	if showName == "":
		allShows = Show.objects.order_by('name')
		return render(request, 'hades/video.html', {
			'allShows': allShows
		})

	try:
		show = Show.objects.get(name=showName)
	except(Show.DoesNotExist):
		messages.error(request, "Show '%s' does not exist" % (showName))
		return redirect('hades:video')

	episodes = Episode.objects.filter(show=show).order_by('season', 'number')

	return render(request, 'hades/show.html', {
		'showName': showName,
		'show': show,
		'episodes': episodes,
	})

@login_required
def sudoku(request):
	data = readSudoku()
	return render(request, "hades/sudoku.html", {
		'size': range(9),
		'data': data,
	})

def readSudoku():
	return [[0,0,3,9,0,0,0,5,1],
			[5,4,6,0,1,8,3,0,0],
			[0,0,0,0,0,7,4,2,0],
			[0,0,9,0,5,0,0,3,0],
			[2,0,0,6,0,3,0,0,4],
			[0,8,0,0,7,0,2,0,0],
			[0,9,7,0,0,0,0,0,0],
			[0,0,1,8,2,0,9,4,7],
			[8,5,0,0,0,4,6,0,0]]

class BadRequestCounter(dict):
	def __missing__(self, key):
		return 0

counter = BadRequestCounter()

@cache_control(private=True, max_age=60*60*24)
def notFound(request, message=None):
	ip = request.META['REMOTE_ADDR']
	counter[ip] += 1
	if counter[ip] > 10:
		# do something here #
		return HttpResponse("stop")
	
	if message is None:
		message = "404 - Page not found"

	time = timezone.now()
	print("Not found request from: " + ip)
	return render(request, "hades/notFound.html", {
		'ip' : ip,
		'time': time,
		'message': message,
	})
