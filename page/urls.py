from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'page'
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/portfolio-details/<int:pk>', views.portfolio_details, name='portfolio-details'),
    path('contact/', views.contact, name='contact'),
    path('message/', views.contact, name='message'),
]
