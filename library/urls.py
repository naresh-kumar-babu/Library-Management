from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('delete-book/<int:book_id>/', views.book_del_handler),
    path('add-book/', views.add_book, name='add-book'),
    path('borrows/', views.borrows, name='borrows'),
]
