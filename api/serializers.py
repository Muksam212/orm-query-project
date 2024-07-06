from rest_framework import serializers
from query.models import *

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = (
            'id',
            'name',
            'age',
            'company',
            'languages'
        )

class CompanySerializer(serializers.ModelSerializer):
    programmer = ProgrammerSerializer(many = True)
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'location',
            'date_created',
            'programmer'
        )

class LanguageSerializer(serializers.ModelSerializer):
    programmers = ProgrammerSerializer(many = True)
    class Meta:
        model = Language
        fields = (
            'id',
            'name',
            'creator',
            'paradigm',
            'date_created',
            'programmers'
        )