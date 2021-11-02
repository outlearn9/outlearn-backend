from django.db import models
from django.contrib import admin
from .tags import *

class Courses(models.Model):
    course_name = models.CharField(max_length=20, blank=False, default='')
    description=models.CharField(max_length=300, blank=False, default='')
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True, blank=True)
    is_certificate= models.BooleanField(default=False)
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE)

    class Meta:
        db_table = "course"
    def __str__(course_name):
        """String for representing the Model object."""
        return self.tag
class CourseAdmin(admin.ModelAdmin):
     model = Courses
     exclude = ('created_at','updated_at','is_deleted')