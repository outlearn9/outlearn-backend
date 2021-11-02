from django.db import models
from .  import specialisationModel
from . import higherStudyModel
class Visitor(models.Model):
    visitor_id =  models.CharField(max_length=150, blank=False, default='')
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    created_at=  models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=  models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "visitor_info" 





        

class VisitorDetails(models.Model):
    visitor = models.ForeignKey(Visitor,on_delete=models.CASCADE)
    specialisation = models.ForeignKey(specialisationModel.Specialization,on_delete=models.CASCADE)
    higher_studies =  models.ForeignKey(higherStudyModel.HigherStudy,on_delete=models.CASCADE)
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    created_at=  models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=  models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "visitor_details" 


class User(models.Model):
    email =      models.CharField(max_length=150,default='')
    contact =    models.BigIntegerField()
    name  =      models.CharField(max_length=150,blank=False,default='')
    is_whatsapp_number=models.IntegerField(default=0)
    visitor = models.ForeignKey(Visitor,on_delete=models.CASCADE)
    working_status= models.IntegerField()
    working_year= models.IntegerField(default=0)
    start_year=models.IntegerField(default=0)
    end_year=models.IntegerField(default=0)
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    created_at=  models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=  models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "user"

class OneTimePassword(models.Model):
    contact = models.BigIntegerField()
    otp =  models.IntegerField()
    is_active =  models.BooleanField(default=True)
    is_deleted =  models.BooleanField(default=False)
    created_at=  models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=  models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = "one_time_password"