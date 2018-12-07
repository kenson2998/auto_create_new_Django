pip install -r requirements.txt
django-admin startproject %1
python %cd%\%1\manage.py migrate
cd %1
python manage.py startapp %2
cd ..
python set_evn.py %1 %2
del %cd%\%1\%2\tests.py
del %cd%\%1\%2\views.py
mkdir %cd%\%1\%1\templates
start start-django.bat %1
timeout /t 2
start chrome localhost
