import subprocess
import sys
#sys.argv[1]

pj_name=input(u'命名專案名稱(不能中文):')
app_name=input(u'命名應用名稱(不能中文):')
a=subprocess.Popen('django.bat '+pj_name+' '+app_name)