import subprocess
import sys
#sys.argv[1]
app_path=sys.argv[1]+r'\\'+sys.argv[1]
app_name=sys.argv[1]
app_path2=sys.argv[1]+r'\\'+sys.argv[2]

########     settings.py
data = ["'django.contrib.staticfiles',","TIME_ZONE = 'UTC'","STATIC_URL = '/static/'"]


word=["TIME_ZONE = 'Asia/Taipei'","STATIC_ROOT = 'static'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)"]
rewrite = ''
with open(app_path+r'\settings.py', 'r+') as f:
    for line in f:
        if data[0] in line:
            rewrite += line + "    '"+app_name+"',"
        elif data[1] in line:
            rewrite += word[0]+ "\n"
        elif data[2] in line:
            rewrite += line+ "\n"+ word[1]+ "\n"+word[2]
        else:
            rewrite += line

f.close()
w = open(app_path+ r'\settings.py', 'w')
w.write(rewrite)
w.close()


########      wsgi.py
rewrite = ''
data1=['from django.core.wsgi import get_wsgi_application','application = get_wsgi_application()']
wite=['from whitenoise.django import DjangoWhiteNoise','from dj_static import Cling','application = DjangoWhiteNoise(application)']
with open(app_path+r'\wsgi.py', 'r+') as f:
    for line in f:
        if data1[0] in line:
            rewrite += line + "\n"+wite[0]+"\n"+wite[1]
        elif data[1] in line :
            rewrite += line + "\n"+wite[2]
        else:
            rewrite += line

f.close()

w = open(app_path+r'\wsgi.py', 'w')
w.write(rewrite)
w.close()



########      urls.py

data2=['from django.contrib import admin',"url(r'^admin/', include(admin.site.urls)),"]
word=['from '+sys.argv[1]+'.views import *\n',"    url(r'^$', index),\n"]
rewrite = ''
with open(app_path+r'\urls.py', 'r+') as f:
    for line in f:
        if data2[0] in line:
            rewrite += line +'\n'+word[0]
        elif data2[1] in line:
            rewrite += line + '\n' + word[1]
        else:
            rewrite += line

f.close()

w = open(app_path+r'\urls.py', 'w')
w.write(rewrite)
w.close()

########      views.py
data3=['from django.shortcuts import render','# Create your views here.']
word=['from django.shortcuts import render, render_to_response, HttpResponse, redirect',"def index(request):",
    r"    return HttpResponse('Hello ! This is "+sys.argv[2]+" app homepage!')"]
rewrite = ''
with open(app_path2+r'\views.py', 'r+') as f:
    for line in f:
        if data3[0] in line:
            rewrite += line +'\n'+ word[0]
        elif data3[1] in line:
            rewrite += line + '\n' + word[1]+ '\n'+word[2]
        else:
            rewrite += line

f.close()

w = open(app_path+r'\views.py', 'w')
w.write(rewrite)
w.close()
