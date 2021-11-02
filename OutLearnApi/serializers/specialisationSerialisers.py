from rest_framework import serializers 
from ..models import *
 
 
class SpecializationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Specialization
        fields = ('id',
                  'speicialization',
                  'is_active',
                  'is_deleted',
                  'created_at',
                  'updated_at'
                  )

class CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields = ('id',
                  'category',
                  'is_active',
                  'is_deleted',
                  'created_at',
                  'updated_at'
                  )
class SkillSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Skill
        fields = ('id',
                  'skill',
                  'is_active',
                  'is_deleted',
                  'created_at',
                  'updated_at'
                  )
