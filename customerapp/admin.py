from django.contrib import admin
from .models import PhoneNumber,CustomerRecord
# Register your models here.

admin.site.register(PhoneNumber)
admin.site.register(CustomerRecord)
