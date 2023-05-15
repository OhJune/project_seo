from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main_page'

urlpatterns = [
    path('', views.main, name='main'), # 127.0.0.1로 접속하면 알아서 main_page url로 이동하여서 여기까지 왔고 이제 views.py의 main함수로 가!
    path('profile/',views.profile, name='profile'), # 127.0.0.1/profile/로 접속하면 알아서 views.py의 profile함수로 가!
    path('quotes/',views.quotes, name='quotes'), # 127.0.0.1/quotes/로 접속하면 알아서 views.py의 quotes함수로 가!
    path('rolling/',views.rolling, name='rolling'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)