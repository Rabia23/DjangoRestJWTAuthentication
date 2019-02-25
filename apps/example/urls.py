from django.conf.urls import url
from apps.example import views

urlpatterns = [
    url(r'^', views.IndexView.as_view(), name='index'),
]
