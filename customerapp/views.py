from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import PhoneNumber, CustomerRecord
from .serializers import PhoneNumberSerializer, CustomerRecordSerializer

class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

class CustomerRecordViewSet(viewsets.ModelViewSet):
    queryset = CustomerRecord.objects.all()
    serializer_class = CustomerRecordSerializer

    def list_by_phone_number(self, request, phone_number):
        # filter the customer records with phonenumber 
        queryset = CustomerRecord.objects.filter(phone_number__phone_number=phone_number)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def list_by_week(self, request, week):

        # filter the customer records with week 
        queryset = CustomerRecord.objects.filter(week=week)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def list_by_month(self, request, month):
        # filter the customer records with month 
        queryset = CustomerRecord.objects.filter(month=month)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

