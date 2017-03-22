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
from .models import Blog, PageView
from .forms import BlogForm

# Misc. imports #
import datetime, time

pageSize = 2

def incrementPageView(name):
    pageView = PageView.objects.filter(page_name=name).first()
    if pageView is None:
        pageView = PageView(page_name=name)
    pageView.page_count += 1
    pageView.save()

# View functions #
def index(request):
    incrementPageView('index')
	return render(request, 'hades/index.html')

def blog(request, page=-1):
	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			submitBlogFromRequest(request)
			return redirect('hades:blog')
	else:
	    incrementPageView('blog')
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

def nerdy(request):
    incrementPageView('nerdy')
    return render(request, 'hades/nerdy.html')


class BadRequestCounter(dict):
	def __missing__(self, key):
		return 0

counter = BadRequestCounter()

@cache_control(private=True, max_age=60*60*24)
def notFound(request, message=None):
    incrementPageView('404')
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
