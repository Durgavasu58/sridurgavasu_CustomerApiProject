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

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        record = queryset.filter(pk=pk).first()
        if record:
            serializer = self.get_serializer(record)
            return Response(serializer.data)
        else:
            return Response({"error": "Record not found"}, status=404)

    def list_by_phone_number(self, request, phone_number):
        queryset = CustomerRecord.objects.filter(phone_number__phone_number=phone_number)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def list_by_week(self, request, week):
        queryset = CustomerRecord.objects.filter(week=week)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def list_by_month(self, request, month):
        queryset = CustomerRecord.objects.filter(month=month)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

