from django.urls import path
from . import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('processing_1/', views.send, name='send'),
 	path('error_404/', views.services_search_mobile, name='services_search_mobile'),
 	# path('', views.form_services, name='form_services'),
]