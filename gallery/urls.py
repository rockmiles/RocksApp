from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('details/', views.postdetail, name='post-page')
]
