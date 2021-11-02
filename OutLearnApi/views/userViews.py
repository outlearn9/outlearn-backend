from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.db import connection
from ..models import *
from ..serializers import *
from rest_framework.decorators import api_view
from  ..util import customFunction
from  ..constants import constants
from  ..constants import messages
from django.db.models import Q
from django.contrib.auth import authenticate
# Create your views here.
@api_view(['POST'])
def save_visitor_info(request):
    # Save visitor info 
    if request.method == 'POST':
        visitor_data = JSONParser().parse(request)
        visitor_serializer = VisitorSerializer(data=visitor_data)
        if visitor_serializer.is_valid():
            visitor=visitor_serializer.save()
            final_visitor_data={'visitor':visitor.id,'specialisation':visitor_data['specialisation_id'],'higher_studies':visitor_data['higher_studies_id']}
            final_visitor_serializer=VisitorDetailsSerializer(data=final_visitor_data)
            if final_visitor_serializer.is_valid():
              final_visitor=final_visitor_serializer.save()
            return  customFunction.send_response(request,'true',status.HTTP_201_CREATED,messages.save_success,{},'')
        return customFunction.send_response(request,'false',status.HTTP_400_BAD_REQUEST,messages.error_message,visitor_serializer.errors,messages.error_message)   
# save user profile 
@api_view(['POST'])
def save_user(request):
    if request.method=='POST':
        request_data=JSONParser().parse(request)
        visitor_data = Visitor.objects.filter(visitor_id=request_data['visitor_id']).values_list('id', flat=True)
        if len(visitor_data)>0:
          user_data= User.objects.filter(visitor_id=visitor_data[0]).values_list('id', flat=True)
          contact_exist=User.objects.filter(contact=request_data['contact']).values_list('id', flat=True)
          email_exist=User.objects.filter(email=request_data['email']).values_list('id', flat=True)
          if len(contact_exist)>0:
              return  customFunction.send_response(request,'false',status.HTTP_400_BAD_REQUEST,messages.contact_already_exist,{},'')
          elif len(email_exist)>0:
              return  customFunction.send_response(request,'false',status.HTTP_400_BAD_REQUEST,messages.email_already_exist,{},'')
          elif len(user_data)>0:
              User.objects.filter(id=user_data[0]).update(visitor_id=visitor_data[0])
              return  customFunction.send_response(request,'true',status.HTTP_201_CREATED,messages.save_success,{},'')                        
          else:
              user_data={'visitor':visitor_data[0]}
              request_data.update(user_data)
              user_serializer=UserSerializer(data=request_data)
              if user_serializer.is_valid():
                    user=user_serializer.save()
                    return  customFunction.send_response(request,'true',status.HTTP_201_CREATED,messages.save_success,{},'')
              return customFunction.send_response(request,'false',status.HTTP_400_BAD_REQUEST,messages.error_message,user_serializer.errors,messages.error_message)   
        else:
         return customFunction.send_response(request,'false',status.HTTP_400_BAD_REQUEST,messages.visitor_error_message,{},messages.error_message)  


#send Otp 
@api_view(['POST'])
def send_otp(request):
    if request.method=='POST':
      request_data=JSONParser().parse(request)
      user_data = User.objects.filter(contact=request_data['contact']).values_list('id', flat=True)
      if len(user_data)>0:
        otp_data={'otp':1234}
        request_data.update(otp_data)
        otp_serializer=OneTimePasswordSerializer(data=request_data)
        if otp_serializer.is_valid():
            otp_entry_exist= OneTimePassword.objects.filter(contact=request_data['contact']).values_list('id', flat=True)
            if len(otp_entry_exist)>0:
             otp_edit = OneTimePassword.objects.get(contact=request_data['contact']) # object to update
             otp_edit.otp = 1234 # update otp
             otp_edit.save() # save object 
             return  customFunction.send_response(request,'true',status.HTTP_201_CREATED,messages.otp_sent_success,{},'')
            else:
             one_time_password=otp_serializer.save()
             return  customFunction.send_response(request,'true',status.HTTP_201_CREATED,messages.otp_sent_success,{},'')
        return customFunction.send_response(request,'false',status.HTTP_400_BAD_REQUEST,messages.error_message,otp_serializer.errors,messages.error_message)   
      else:
        return customFunction.send_response(request,'false',status.HTTP_400_BAD_REQUEST,messages.user_not_exist,{},messages.user_not_exist)  
  
#verify otp
@api_view(['POST'])
def verify_otp(request):
    if request.method=='POST':
      request_data=JSONParser().parse(request)
      otp_serializer=OneTimePasswordSerializer(data=request_data)
      if otp_serializer.is_valid():
            otp_data = OneTimePassword.objects.filter(Q(otp=request_data['otp']) & Q(contact=request_data['contact'])).values_list('id', flat=True)
            if len(otp_data)>0:
              contact=request_data['contact']
              query='select id,contact,email,name,is_whatsapp_number from user where contact=%s'
              user_result=customFunction.create_custom_query(query,contact)
              # payload_data={
              #   "pk":user_result[0][0],
              #   "username":user_result[0][1],
              #   "email":user_result[0][2]
              # }
              payload_data=payLoad(user_result[0][0],user_result[0][1],user_result[0][2])
              # user = authenticate(username=email, password=password)
              token=customFunction.create_jwt_token(payload_data)
              final_user_object={
                'user_id':user_result[0][0],
                 'contact':user_result[0][1],
                 'email':user_result[0][2],
                 'name':user_result[0][3],
                 'is_whatsapp_number':user_result[0][4],
                'token':token
              }
              return  customFunction.send_response(request,'true',status.HTTP_201_CREATED,messages.otp_verified,final_user_object,'')
            else:
              return  customFunction.send_response(request,'false',status.HTTP_201_CREATED,messages.otp_verify_fail,{},'')
      return customFunction.send_response(request,'false',status.HTTP_400_BAD_REQUEST,messages.error_message,otp_serializer.errors,messages.error_message)   

class payLoad:
    def __init__(self, pk, username,email):
      self.pk = pk
      self.username = username

      self.email = email
    