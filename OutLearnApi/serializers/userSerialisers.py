from rest_framework import serializers 
from ..models import *
 
class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ('id',
                  'visitor_id',
                  'is_active',
                  'is_deleted',
                  'created_at',
                  'updated_at'
                  )
class VisitorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorDetails
        fields = ('id',
                  'visitor',
                  'specialisation',
                   'higher_studies',
                  'is_active',
                  'is_deleted',
                  'created_at',
                  'updated_at'
                  )
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'visitor',
                  'email',
                   'contact',
                   'name',
                   'is_whatsapp_number',
                   'working_status',
                   'working_year',
                   'start_year',
                   'end_year',
                  'is_active',
                  'is_deleted',
                  'created_at',
                  'updated_at'
                  )
class OneTimePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneTimePassword
        fields = ('id',
                  'contact',
                  'otp',
                  'is_active',
                  'is_deleted',
                  'created_at',
                  'updated_at'
                  )