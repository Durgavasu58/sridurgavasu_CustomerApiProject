# importdata/management/commands/import_data.py
import csv
from django.core.management.base import BaseCommand
from customerapp.models import PhoneNumber, CustomerRecord

class Command(BaseCommand):
    help = 'Import data from text files'

    def handle(self, *args, **options):
        # Path to your text files
        phone_numbers_file = 'phone_numbers.txt'
        customer_records_file = 'customer_records.txt'

        # Import phone numbers
        with open(phone_numbers_file, 'r') as file:
            next(file)
            for line in file:
                phone_number = line.strip()
                PhoneNumber.objects.get_or_create(phone_number=phone_number)

        # Import customer records
        with open(customer_records_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) == 6:  # Ensure the row has all 6 fields
                    username, phone_number, call_duration, call_type, month, week = row
                    customer_record = CustomerRecord.objects.create(
                        username=username,
                        phone_number=PhoneNumber.objects.get(phone_number=phone_number),
                        call_duration=int(call_duration),
                        call_type=call_type,
                        month=month,
                        week=week
                    )
                    customer_record.save()
                else:
                    print(f"Ignoring invalid row: {row}")