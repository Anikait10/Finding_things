from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('new_search', views.new_search, name = 'new_search'),
]
