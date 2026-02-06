from django.contrib import admin

# Register your models here.
from .models import Student,Product,StudentProfile,Category,Service

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)