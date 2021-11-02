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
def specialisation_list(request):
    # GET list of master data of specialisations
    if request.method == 'GET':
        specialisations = Specialization.objects.all()
        speicialisation_serializer = SpecializationSerializer(specialisations,many=True)
        return  customFunction.send_response(request,'true',constants.success,messages.success_message,speicialisation_serializer.data,'')

def category_list(request):
    # GET list of master data of specialisations
    if request.method == 'GET':
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(category_serializer.data, safe=False)

def get_specialisation(request):
    # GET list of master data of specialisations
    if request.method == 'GET':
        query= 'Select ssc.id,os.speicialization,s.skill,c.category from OutLearnApi_skillwithspecializationandcategory as ssc inner join OutLearnApi_specializationwithcategory  as sc on ssc.specialization_category_id=sc.id inner join OutLearnApi_category as c on sc.category_id=c.id inner join OutLearnApi_skill as s on ssc.skill_id=s.id inner join OutLearnApi_specialization as os on sc.specialization_id=os.id'
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        final={
            'success':'true',
            'status': 200,
            'message':'Record Fetch Successfully',
            'data':row
        }
        return JsonResponse(final, safe=False)
 