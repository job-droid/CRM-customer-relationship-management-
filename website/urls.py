from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.login_user, name='login'),
    path('', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register_user')
]
