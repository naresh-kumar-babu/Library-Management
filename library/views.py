from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Book, Borrow
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your views here.
def home(request):
    book_count = Book.objects.count
    borrow_count = Borrow.objects.count

    pending_returns = 0

    # Total fine calculation
    students = list(Student.objects.filter().values_list('fine_amount', flat=True))
    total_fine = sum(students)

    #Finding the pending returns
    for s in students:
        if s != 0:
            pending_returns += 1

    return render(request, 'library/index.html', {'book_count': book_count, 'borrow_count': borrow_count, 'total_fine': total_fine, 'pending_returns':pending_returns})

def books(request):
    books = Book.objects.all()
    return render(request, 'library/books.html', {'books': books})

def students(request):
    students = Student.objects.all()
    return render(request, 'library/students.html', {'students': students})

def borrows(request):
    borrows = Borrow.objects.all()
    return render(request, 'library/borrows.html', {'borrows': borrows})

def book_del_handler(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('books')

def student_del_handler(request, student_id):
    Student.objects.get(id=student_id).delete()
    return redirect('students')

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn_number = request.POST.get('isbn_number')
        copies = request.POST.get('copies')
        book = Book(
            isbn_number=isbn_number,
            title=title,
            author=author,
            copies=copies
            )
        book.save()
        return redirect('books')
    return render(request, 'library/add-book.html')

def add_student(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        roll_number = request.POST.get('roll_number')
        academic_year = request.POST.get('academic_year')
        email = roll_number.lower() + '@ch.students.amrita.edu'
        student = Student(
            fullname=fullname,
            roll_number=roll_number,
            academic_year=academic_year,
            email=email
        )
        student.save()
        return redirect('home')
    return render(request, 'library/add-student.html')

