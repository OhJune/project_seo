from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import QuestionForm
# Create your views here.

def main(request):
    return render(request, 'main_page/main.html')

def rolling(request):
    return render(request, 'main_page/question_detail.html')

def profile(request):
    return render(request, 'main_page/profile.html')

def quotes(request):
    return render(request, 'main_page/quotes.html')

def detail(request, question_id):
    """
    내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'main_page/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    """
    롤링페이퍼 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # 추가한 속성 author 적용
            question.create_date = timezone.now()
            question.save()
            return redirect('main_page:main')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'main_page/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    롤링페이퍼 수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('main_page:detail', question_id=question.id)


    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('main_page:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'main_page/question_form.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    답변등록
    """
    print(request.method)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # 추가한 속성 author 적용
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('main_page:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'main_page/question_detail.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('main_page:detail', question_id=question.id)
    question.delete()
    return redirect('main_page:main')

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('main_page:detail', question_id=answer.question.id)


    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('main_page:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'main_page/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('main_page:detail', question_id=answer.question.id)