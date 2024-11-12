import copy

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

QUESTIONS = [
    {
        'title': f'Title {i + 1}',
        'id': i,
        'text': f'This is text for question # {i + 1}'
    } for i in range(30)
]


def pagination(request, quest):
    try:
        page_num = int(request.GET.get('page', 1))
    except ValueError:
        page_num = 1
    paginator = Paginator(quest, 5)
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)

    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page


def index(request):
    page = pagination(request, QUESTIONS)
    return render(
        request,
        'index.html',
        context={'questions': page.object_list, 'page_obj': page}
    )


def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    page = pagination(request, hot_questions)

    return render(
        request,
        'hot.html',
        context={'questions': page.object_list, 'page_obj': page}
    )


def question(request, question_id):
    try:
        question_id = int(question_id)
        one_question = QUESTIONS[question_id]
    except (IndexError, ValueError):
        one_question = None
    if question_id > 0:
        prev_question_id = question_id - 1
    else:
        prev_question_id = None
    if question_id < len(QUESTIONS) - 1:
        next_question_id = question_id + 1
    else:
        next_question_id = None
    return render(
        request,
        'one_question.html',
        {
            'item': one_question,
            'prev_question_id': prev_question_id,
            'next_question_id': next_question_id
        }
    )


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'registration.html')


def ask(request):
    return render(request, 'ask.html')


def setting(request):
    return render(request, 'settings.html')


def single(request):
    return render(request, 'single.html')


def registration(request):
    return render(request, 'registration.html')


def tag(request):
    page = pagination(request, QUESTIONS)
    return render(
        request,
        'tags.html',
        context={'questions': page.object_list, 'page_obj': page}
    )
