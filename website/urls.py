from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.login_user, name='login'),
    path('', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register_user'),
    path('customer/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_customer, name="delete_record"),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:pk>', views.update_customer, name="update_customer")
]
