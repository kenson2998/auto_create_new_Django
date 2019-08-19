import os, shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

os.system('pip install -r requirements.txt')
T = True
while T:
    pj_name = input('命名專案名稱(不能中文):')
    app_name = input('命名應用名稱(不能中文):')
    proj_dir = os.path.join(BASE_DIR, pj_name)
    if os.path.exists(proj_dir):
        print('django專案:%s已存在\n' % pj_name)
    else:
        T = False
pro_set_dir = os.path.join(proj_dir, pj_name)
app_path = os.path.join(proj_dir, app_name)
os.system('django-admin startproject %s' % pj_name)
os.system(r'python %s\manage.py migrate' % proj_dir)
os.system(r'python %s\manage.py startapp %s' % (proj_dir, app_name))
shutil.copytree(app_name, app_path)
shutil.rmtree(app_name)

########     settings.py
data = ["'django.contrib.staticfiles',", "TIME_ZONE = 'UTC'", "STATIC_URL = '/static/'", "'DIRS': [],"]
word = ["TIME_ZONE = 'Asia/Taipei'\n", "STATIC_ROOT = 'static'", "STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)","'DIRS': [os.path.join(BASE_DIR, 'templates')],\n"]

rewrite = ''
with open(pro_set_dir + r'\settings.py', 'r+') as f:
    for line in f:
        if data[0] in line:
            rewrite += line + "    '%s',\n" % app_name
        elif data[1] in line:
            rewrite += word[0]
        elif data[2] in line:
            rewrite += "%s\n%s\n%s" % (line, word[1], word[2])
        elif data[3] in line:
            rewrite += word[3]
        else:
            rewrite += line

with open(pro_set_dir + r'\settings.py', 'w') as wf:
    wf.write(rewrite)

# shutil.rmtree(proj_dir)

#
########      wsgi.py
rewrite = ''
data1 = ['from django.core.wsgi import get_wsgi_application', 'application = get_wsgi_application()']
wite = ['from whitenoise.django import DjangoWhiteNoise', 'from dj_static import Cling',
        'application = DjangoWhiteNoise(application)']
with open(pro_set_dir + r'\wsgi.py', 'r+') as f:
    for line in f:
        if data1[0] in line:
            rewrite += "%s\n%s\n%s" % (line, wite[0], wite[1])
        elif data[1] in line:
            rewrite += "%s\n%s" % (line, wite[2])
        else:
            rewrite += line

with open(pro_set_dir + r'\wsgi.py', 'w') as w:
    w.write(rewrite)

#
########      urls.py

data2 = ['from django.contrib import admin', "url(r'^admin/', include(admin.site.urls)),"]
word = ['from %s import views\n' % app_name, "    url(r'^$', views.index),\n"]
rewrite = ''
with open(pro_set_dir + r'\urls.py', 'r+') as f:
    for line in f:
        if data2[0] in line:
            rewrite += '%s\n%s' % (line, word[0])
        elif data2[1] in line:
            rewrite += '%s\n%s' % (line, word[1])
        else:
            rewrite += line

with open(pro_set_dir + r'\urls.py', 'w') as w:
    w.write(rewrite)

#
########      views.py
data3 = ['from django.shortcuts import render', '# Create your views here.']
word = ['from django.shortcuts import render, render_to_response, HttpResponse, redirect', "def index(request):",
        r"    return HttpResponse('Hello ! This is %s app homepage!')" % app_name]
rewrite = ''
with open(app_path + r'\views.py', 'r+') as f:
    for line in f:
        if data3[0] in line:
            rewrite += '%s\n%s' % (line, word[0])
        elif data3[1] in line:
            rewrite += '%s\n%s\n%s' % (line, word[1], word[2])
        else:
            rewrite += line

with open(app_path + r'\views.py', 'w') as w:
    w.write(rewrite)

os.system(r'mkdir %s\templates' % proj_dir)
os.system(r'mkdir %s\static' % proj_dir)
os.system(r'python %s\manage.py runserver 80' % proj_dir)
