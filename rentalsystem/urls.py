# helloworld_project/urls.py
from django.contrib import admin
from django.urls import path, include

from pages.views import home
from pages import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('pages.urls')),
    path('', views.home),
    path('signup.html/', views.signup),
    path('signin.html/', views.signin),
    path('about.html/', views.about),

    # path('home/home.html/', views.signin),
    # path('signin/', views.main)
]
