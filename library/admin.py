from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Borrow)