from rest_framework import serializers
from .models import PhoneNumber, CustomerRecord

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number']

class CustomerRecordSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberSerializer() 
    class Meta:
        model = CustomerRecord
        fields = ['username', 'phone_number', 'call_duration', 'call_type', 'month', 'week']
