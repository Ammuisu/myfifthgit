from django.urls import path
from app2.views import *
app_name="something"

urlpatterns=[
   path('jinja_app2/',jinja_app2,name="jinja_app2"),
 ]