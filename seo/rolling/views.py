from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .forms import QuestionForm, AnswerForm
from .models import Question, Answer




from django.http import HttpResponse


def index(request):
    article = '''
    <h1>여기에 원래 저희가 쓴 감동의 롤링페이퍼가<br>pybo 게시판 형식으로 구현되어 있었는데요..</h1> 
    <h1>저희가 쓴 AWS RDS 서버가 해킹을 당해서 날라갔습니다....</h1>
    <img src="/static/img/해킹.png" alt="My img">
    <h1>이거 끝나면 다시 연결할 수 있게 도와주세요ㅠ</h1>
    '''
    return HttpResponse(HTMLTemplate(article))
