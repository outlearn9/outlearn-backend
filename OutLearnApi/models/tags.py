from django.db import models
from django.contrib import admin

class Tags(models.Model):
    tag = models.CharField(max_length=20, blank=False, default='')
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "tag"
    def __str__(self):
        """String for representing the Model object."""
        return self.tag
class TagAdmin(admin.ModelAdmin):
     model = Tags
     exclude = ('created_at','updated_at','is_deleted')