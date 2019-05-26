from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('movies', views.MovieList.as_view(), name = 'Movie List'),
    path('movie/<int:pk>', views.DetailView.as_view(), name = 'Movie Detail'),
]