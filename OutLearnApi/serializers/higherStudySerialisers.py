from rest_framework import serializers 
from ..models import *
 
class HigherStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = HigherStudy
        fields = ('id',
                  'name',
                  'is_active',
                  'is_deleted',
                  'created_at',
                  'updated_at'
                  )