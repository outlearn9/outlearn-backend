from django.db import models
from django.contrib import admin

class HigherStudy(models.Model):
    name = models.CharField(max_length=150, blank=False, default='')
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "higher_study"
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class HigherStudyAdmin(admin.ModelAdmin):
     model = HigherStudy
     exclude = ('created_at','updated_at','is_deleted')
