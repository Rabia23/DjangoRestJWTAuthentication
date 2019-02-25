from django.conf.urls import url
from apps.authentication import views

urlpatterns = [
    url(r'^register/', views.RegistrationView.as_view(), name='register'),
    url(r'^login/', views.LoginView.as_view(), name='login')
]
