from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    return JsonResponse( {"hi":"hi"})

def results(request, question_id:int):
    return JsonResponse( {f"question_id {question_id}":"results"})

def detail(request, question_id:int):
    return JsonResponse( {f"question_id {question_id}":"detail"})

def vote(reqest, question_id:int):
    return JsonResponse( {f"question_id {question_id}":"vote"})