from django.contrib import admin
from django.urls import path,include
from restaurant import views

app_name='restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogDetails/', views.blogDetails, name='Blog-Details'),
    path('blogHome/', views.blogHome, name='Blog-Home'),
    path('contactUs/',views.contactUs, name='Contact-Us'),
    path('menu/',views.menu, name="Menu"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('logout/',views.logout,name="logout"),
    path('bookTable/',views.table,name="bookTable"),
    #path('register/',views.register,name='register'),
    path('checkout/',views.checkout,name="checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("tracker/", views.tracker, name="TrackingStatus"),

]