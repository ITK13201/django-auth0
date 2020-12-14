from django.shortcuts import render
from django.views import generic

# Create your views here.
class MypageView(generic.TemplateView):
    template_name = 'mypage/mypage.html'