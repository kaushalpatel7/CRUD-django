from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    
    path("",views.home,name=""),
    
    path("register",views.register,name="register"),
    
    path("my-login",views.my_login,name="my-login"),
    
    path("user-logout",views.user_logout,name="user-logout"),
    
    
    # Urls for CRUD operation
     path("dashboard",views.dashboard,name="dashboard"),
    
    path("create-record",views.create_record,name="create-record"),
    
    path("update-record/<int:pk>",views.update_recors,name="update-record"),
    
    path("view-record/<int:pk>",views.singular_record,name="record"),
    
    path("delete-record/<int:pk>",views.delete_record,name="delete-record"),
    
    
]