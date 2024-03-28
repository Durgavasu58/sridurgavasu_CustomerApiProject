Note:- shared the ".env"  file of the project conifgurations in respective email  

Installation steps:

1.create a virtual environment 
  --> pip install virtualenv
	
  --> virtualenv "env"
	
  --> source env/bin/activate
	
2. clone or pull the repistory and in the project directory
   run the command 
   --> pip install -r requirements.txt
3. --> python manage.py makemigrations && python manage.py migrate
4. create a superuser for admin interface
  --> python manage.py createsuperuser

Added a text files of phonenumber and customerdata file in code repo need to import into the database, default db.sqlite3  i used
For script i added CustomDjango Management Command

1. customerapp/management/commands/import_data.py
run the command

--> python manage.py import_data

once the command is run data will be imported to database


APIS:-

1.http://127.0.0.1:8000/phone_numbers/   "Fetch all phonenumber records"

2.http://127.0.0.1:8000/customer_records/  "Fetch all customer records"

"Fetch records by phonenumber, week, month"

3. http://127.0.0.1:8000/customer_records/by_phone_number/1234567890/

4. http://127.0.0.1:8000/customer_records/by_week/week4/

6. http://127.0.0.1:8000/customer_records/by_month/may/
   

   
