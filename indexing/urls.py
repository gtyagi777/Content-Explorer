from django.urls import path

from indexing import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('user/<str:username>', views.user_page, name = 'user_page')
]