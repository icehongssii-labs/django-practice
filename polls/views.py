from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Questions, Choices


def index(request):
    latest_question_list = Questions.objects.all().order_by("-pub_date")[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def results(request, question_id:int):
    return JsonResponse( {f"question_id {question_id}":"results"})

def detail(request, question_id:int):
    question = get_object_or_404(Questions, pk=question_id)    
    return render(request, 'polls/detail.html', {'question':question})

def vote(reqest, question_id:int):
    return JsonResponse( {f"question_id {question_id}":"vote"})