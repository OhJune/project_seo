from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main_page/index.html')

def rolling(request):
    return render(request, 'main_page/rolling_paper.html')

def profile(request):
    return render(request, 'main_page/profile.html')

def quotes(request):
    return render(request, 'main_page/quotes.html')

def main(request):
    return render(request, 'main_page/main.html')