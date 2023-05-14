<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def main(request):
    return render(request, 'main_page/main.html')
=======
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from common.views import signup

@login_required
def index(request):
    return render(request, 'main_page/index.html')

def rolling(request):
    return render(request, 'main_page/rolling_paper.html')
>>>>>>> 0846c43897bbe12644ec604bf785140197af2dcd

@login_required
def profile(request):
    return render(request, 'main_page/profile.html')

@login_required
def quotes(request):
    return render(request, 'main_page/quotes.html')

