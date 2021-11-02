from django.db import models
from django.contrib import admin


class Category(models.Model):
    category = models.CharField(max_length=150, blank=False, default='')
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "category"
    def __str__(self):
        return self.category


class CategoryAdmin(admin.ModelAdmin):
     model = Category
     exclude = ('created_at','updated_at','is_deleted')

# Create your models here.
class Specialization(models.Model):
    speicialization = models.CharField(max_length=150, blank=False, default='')
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
        #reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", through='SpecializationWithCategory')
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "specialization"
    def __str__(self):
        return self.speicialization

class SpecializationAdmin(admin.ModelAdmin):
     model = Specialization
     exclude = ('created_at','updated_at','is_deleted')



class Skill(models.Model):
    skill = models.CharField(max_length=150, blank=False, default='')
    category = models.ManyToManyField("Category", through='SkillWithSpecializationAndCategory')
    specialization = models.ManyToManyField("Specialization", through='SkillWithSpecializationAndCategory')
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    # category = models.ManyToManyField("Category")
    # Specialization = models.ManyToManyField("Specialization")
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "skill"
    def __str__(self):
        """String for representing the Model object."""
        return self.skill
class SkillAdmin(admin.ModelAdmin):
     model = Specialization
     exclude = ('created_at','updated_at','is_deleted')


class SpecializationWithCategory(models.Model):
    specialization=models.ForeignKey(Specialization,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # specialization_id = models.IntegerField()
    # category_id = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "specilization_category"



class SkillWithSpecializationAndCategory(models.Model):
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization,on_delete=models.CASCADE)

    # specialization_category_id = models.IntegerField()
    # skill_id =  models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "skill_specilization_category"

