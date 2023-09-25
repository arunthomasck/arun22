from. import views
from django.urls import path

urlpatterns = [
    path('',views.demo1,name='demo1'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('details',views.details,name='details'),
    path('single',views.demo2,name='demo2'),
]