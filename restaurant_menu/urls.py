from django.urls import path
from . import views

# Variable name must not change
urlpatterns = [path('', views.MenuList.as_view(), name='home')]
