from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from common.views import signup


def main(request):
    return render(request, 'main_page/main.html')


def profile(request):
    return render(request, 'main_page/profile.html')

def quotes(request):
    return render(request, 'main_page/quotes.html')

