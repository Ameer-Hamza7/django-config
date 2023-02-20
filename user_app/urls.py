from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('unauthorized_user', unauthorized_user, name='unauthorized_user'),
    path('registration', user_registration, name='registration'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('groups-perms', create_company_group, name="groups-perms")
]
