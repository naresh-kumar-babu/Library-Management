from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('students/', views.students, name='students'),
    path('delete-student/<int:student_id>/', views.student_del_handler),
    path('delete-book/<int:book_id>/', views.book_del_handler),
    path('add-book/', views.add_book, name='add-book'),
    path('add-student/', views.add_student, name='add-student'),
    path('add-borrow/', views.add_borrow, name='add-borrow'),
    path('borrows/', views.borrows, name='borrows'),
]
