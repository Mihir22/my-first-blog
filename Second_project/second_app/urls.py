from django.conf.urls import url
from second_app import views

urlpatterns = [url('$',views.form_name_view,name = 'form')]
