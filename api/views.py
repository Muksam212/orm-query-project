from django.shortcuts import render

from .serializers import(
    ProgrammerSerializer,
    LanguageSerializer,
    CompanySerializer
)
from query.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

# Create your views here.

class CompanyList(APIView):
    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = CompanySerializer(Company, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Success"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
        

class CompanyDetails(APIView):
    def get(self, request, id = None):
        company = get_object_or_404(Company, id = id)
        serializer = CompanySerializer(company, many = False)
        return Response(serializer.data)
    
    def put(self, request, id = None):
        company = get_object_or_404(Company, id = id)
        serializer = CompanySerializer(company, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Success"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id = None):
        company = get_object_or_404(Company, id = id)
        serializer = CompanySerializer(company, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Success"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id = None):
        company = get_object_or_404(Company, id = id)
        company.delete()
        return Response({"msg":"Deleted"}, status = status.HTTP_400_BAD_REQUEST)
    

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class LanguageList(ListCreateAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    model = Language

class LanguageDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    model = Language
    lookup_field = "id"


class ProgrammerList(ListCreateAPIView):
    serializer_class = ProgrammerSerializer
    queryset = Programmer.objects.all()
    model = Programmer

class ProgrammerDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgrammerSerializer
    queryset = Programmer.objects.all()
    model = Programmer
    lookup_field = "id"