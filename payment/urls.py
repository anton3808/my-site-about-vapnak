from django.urls import path
from . import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('processing_1/', views.send, name='send'),
 	path('../search/', views.payment_search, name='payment_search'),
 	# path('', views.form_services, name='form_services'),
]