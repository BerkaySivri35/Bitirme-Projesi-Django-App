from django import views
from django.urls import path


from uyelikSistemi import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

]
