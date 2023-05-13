from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index), # 127.0.0.1로 접속하면 알아서 main_page url로 이동하여서 여기까지 왔고 이제 views.py의 index함수로 가!
    path('rolling_paper/',views.rolling), # 127.0.0.1/rolling_page/로 접속하면 알아서 views.py의 rolling함수로 가!
    path('profile/',views.profile), # 127.0.0.1/profile/로 접속하면 알아서 views.py의 profile함수로 가!
    path('quotes/',views.quotes), # 127.0.0.1/quotes/로 접속하면 알아서 views.py의 quotes함수로 가!
    path('main/', views.main),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)