from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def main(request):
    return render(request, 'main_page/main.html')

def profile(request):
    return render(request, 'main_page/profile.html')

def quotes(request):
    return render(request, 'main_page/quotes.html')

