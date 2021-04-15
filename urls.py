from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path

app_name = 'firstApp'

urlpatterns = [
    # Home page
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
