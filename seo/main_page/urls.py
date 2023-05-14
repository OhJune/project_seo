from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main_page'

urlpatterns = [
    path('', views.main, name='main'), # 127.0.0.1로 접속하면 알아서 main_page url로 이동하여서 여기까지 왔고 이제 views.py의 main함수로 가!
    path('rolling_paper/',views.rolling), # 127.0.0.1/rolling_page/로 접속하면 알아서 views.py의 rolling함수로 가!
    path('profile/',views.profile), # 127.0.0.1/profile/로 접속하면 알아서 views.py의 profile함수로 가!
    path('quotes/',views.quotes), # 127.0.0.1/quotes/로 접속하면 알아서 views.py의 quotes함수로 가!
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)