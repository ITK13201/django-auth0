from django.urls import path

from . import views

app_name = 'backend.mypage'
urlpatterns = [
    path('', views.MypageView.as_view(), name='mypage'),
]