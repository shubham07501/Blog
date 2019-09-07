from django.conf.urls import url
from . import views

app_name='home'
urlpatterns=[
	url(r'^$',views.mainpage,name='main'),
	url(r'^about_us/',views.about_us,name='about_us'),
	url(r'^contact_us/',views.contact_us,name='contact_us'),
]