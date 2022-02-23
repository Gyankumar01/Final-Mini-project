# helloworld_project/urls.py
from django.contrib import admin
from django.urls import path, include

from pages.views import home
from pages import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('pages.urls')),
    path('home/', views.home),
    path('home/signup.html/', views.signup)
    path('home/signin.html/', views.signin)
    path('about/', views.about)
    # path('signin/', views.signin),
]
