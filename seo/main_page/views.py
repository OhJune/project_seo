from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main_page/main.html')

def rolling(request):
    return render(request, 'main_page/rolling_paper.html')

def profile(request):
    return render(request, 'main_page/profile.html')

def quotes(request):
    return render(request, 'main_page/quotes.html')