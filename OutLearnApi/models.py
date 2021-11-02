# from django.db import models

# # Create your models here.
# class Specialization(models.Model):
#     speicialization = models.CharField(max_length=150, blank=False, default='')
#     is_active = models.IntegerField()
#     is_deleted = models.IntegerField()
#     created_at= models.DateField()
#     updated_at= models.DateField()


# class Category(models.Model):
#     category = models.CharField(max_length=150, blank=False, default='')
#     is_active = models.IntegerField()
#     is_deleted = models.IntegerField()
#     created_at= models.DateField()
#     updated_at= models.DateField()

# class Skill(models.Model):
#     skill = models.CharField(max_length=150, blank=False, default='')
#     is_active = models.IntegerField()
#     is_deleted = models.IntegerField()
#     created_at= models.DateField()
#     updated_at= models.DateField()

# class SpecializationWithCategory(models.Model):
#     specialization_id = models.IntegerField()
#     category_id = models.IntegerField()
#     created_at= models.DateField()
#     updated_at= models.DateField()

# class SpecializationWithCategory(models.Model):
#     specialization_id = models.IntegerField()
#     category_id = models.IntegerField()
#     created_at= models.DateField()
#     updated_at= models.DateField()

# class SkillWithSpecializationAndCategory(models.Model):
#     specialization_category_id = models.IntegerField()
#     skill_id =  models.IntegerField()
#     created_at= models.DateField()
#     updated_at= models.DateField()

# class HigherStudy(models.Model):
#     name = models.CharField(max_length=150, blank=False, default='')
#     is_active =  models.BooleanField()
#     is_deleted =  models.BooleanField()
#     created_at= models.DateField()
#     updated_at= models.DateField()