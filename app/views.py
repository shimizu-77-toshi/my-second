from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm


def index(request):
    params = {
        "TEXT": "必要な情報を記入してください",
        "TITLE": "占いの部屋",
        "NAME": "占いの世界へようこそ",
        "FORM": TestForm(),
    }
    return render(request, "app/index.html", params)

def ans(name, age, home, hob):
    x = abs(len(name)+int(age)+len(home)+len(hob))
    mod_5 = x % 5
    if mod_5 == 0:
        ans='大吉'
    elif mod_5 == 1:
        ans='中吉'
    elif mod_5 == 2:
        ans='吉'
    elif mod_5 == 3:
        ans='小吉'
    else:
        ans='凶'
    return ans


def form(request):
    name = request.POST["name"]
    age = request.POST["age"]
    hometown = request.POST["hometown"]
    hobey = request.POST["hobey"]

    params = {
        "text": 'あなたの運勢は...',
        "title": "結果は...",
        "ans": ans(name, age, hometown, hobey),
    }
    return render(request, "app/index_ans.html", params)
