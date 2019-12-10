from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'


urlpatterns = [
    url('relative/', views.relativeurltemplate, name='relative'),
    url('other/', views.other, name='other'),
]
