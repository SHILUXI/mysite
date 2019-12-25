import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
sys.path.append('/home/mysite/mysite')
 
from django.core.wsgi import get_wsgi_application
 
application = get_wsgi_application()
