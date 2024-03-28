# telecom/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhoneNumberViewSet, CustomerRecordViewSet

router = DefaultRouter()
router.register('phone_numbers', PhoneNumberViewSet, basename='phone_number')
router.register('customer_records', CustomerRecordViewSet, basename='customer_record')

urlpatterns = [
    path('', include(router.urls)),
    path('customer_records/by_phone_number/<phone_number>/', CustomerRecordViewSet.as_view({'get': 'list_by_phone_number'}), name='customer_records_by_phone_number'),
    path('customer_records/by_week/<week>/', CustomerRecordViewSet.as_view({'get': 'list_by_week'}), name='customer_records_by_week'),
    path('customer_records/by_month/<month>/', CustomerRecordViewSet.as_view({'get': 'list_by_month'}), name='customer_records_by_month'),
]
