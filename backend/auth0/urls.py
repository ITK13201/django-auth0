from django.urls import path

from . import views

app_name = 'backend.auth0'
urlpatterns = [
    path('logout/', views.logout)
]