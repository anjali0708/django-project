from django.conf.urls import url
from app_two import views

urlpatterns = [
    url('' ,views.users,name='users'),
]
