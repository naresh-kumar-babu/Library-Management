from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=200, null=True)
    roll_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    academic_year = models.CharField(max_length=200, 
        choices= (
            ('I year', 'I year'),
            ('II year', 'II year'),
            ('III year', 'III year'),
            ('IV year', 'IV year')
        )
    )
    fine_amount = models.FloatField(null=True)

    def __str__(self):
        return self.fullname

class Book(models.Model):
    isbn_number = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    copies = models.IntegerField(null=True)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    borrower = models.OneToOneField(Student, on_delete=models.CASCADE)
    borrowed_on = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)
    book = models.ManyToManyField(Book)