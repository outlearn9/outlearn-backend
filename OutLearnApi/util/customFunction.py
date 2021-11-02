from django.http.response import JsonResponse
from rest_framework_jwt.settings import api_settings
from django.db import connection
def send_response(request,status,code,message,data,errMessage):
    obj= {
        'success':status,
        'status':code,
        'message':message,
        'error':{
            'err':errMessage,
            'errCode':code
        },
        'data':data
        }
    return JsonResponse(obj, safe=False)

#return jwt token
def create_jwt_token(payload_request):
    JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
    JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
    payload = JWT_PAYLOAD_HANDLER(payload_request)
    print(payload)
    jwt_token = JWT_ENCODE_HANDLER(payload)
    return jwt_token

#create custom query
def create_custom_query(query,param):
     query= query
     cursor = connection.cursor()
     cursor.execute(query,[param])
     row = cursor.fetchall()
     return row