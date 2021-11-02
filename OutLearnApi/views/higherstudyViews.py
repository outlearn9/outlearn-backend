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
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def higher_study_master(request):
    # GET list of master data of specialisations
    if request.method == 'GET':
        higher_study = HigherStudy.objects.all()
        higher_study_serializer = HigherStudySerializer(higher_study, many=True)
        return  customFunction.send_response(request,'true',constants.success,messages.success_message,higher_study_serializer.data,'')

 