from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('borrows/', views.borrows, name='borrows'),
]
