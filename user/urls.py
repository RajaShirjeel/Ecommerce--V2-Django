from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login')
]