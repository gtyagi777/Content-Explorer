from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User 
# Create your views here.


def main_page(request):
    Context = {
        'head_title': 'Django Bookmarks',
        'page_title': 'Welcome to Django Bookmarks',
        'page_body': 'Where you can store and share bookmarks!'
    }
    return render(request, 'main_page.html', Context)

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')
    bookmarks = user.bookmark_set.all()
    Context = {
    'username': username,
    'bookmarks': {}
    }

    return render(request, 'user_page.html', Context)
