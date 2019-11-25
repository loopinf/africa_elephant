import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Board, Card, Column, Card_top30
from . import getdata

import datetime as dt


@ensure_csrf_cookie
def index(request):
    
    input_date = '2019-11-22'
    df = getdata.getdata(input_date)
    Card_top30.objects.all().delete()

    for i in range(0, len(df.index)):
        date = df.iloc[i, 0]
        title = df.iloc[i,1]
        rate = df.iloc[i,2]
        market = df.iloc[i,3]
        Card_top30.objects.create(title=title, rate=rate, market=market)
    
    return render(request, template_name='kanban/base.html', context={
        'boards': Board.objects.all(),
        'tops' : Card_top30.objects.all(),
    })


def new_card(request):
    column_id = int(request.POST.get('column_id'))
    title = request.POST.get('title')
    if title == '':
        return redirect('/')
    assert title and column_id
    Card.objects.create(title=title, column_id=column_id)
    return redirect('/')

def new_list(request):
    board_id = int(request.POST.get('board_id'))
    title = request.POST.get('title')
    if title == '':
        return redirect('/')
    assert title and board_id
    Column.objects.create(title=title, board_id=board_id)
    return redirect('/')

def new_col_name(request):
    column_id = int(request.POST.get('column_id'))
    title = request.POST.get('title')
    if title == '':
        return redirect('/')
    assert title and column_id
    Column.objects.filter(id=column_id).update(title=title)
    return redirect('/')


def view_card(request, card_id, card_slug):
    return render(request, template_name='kanban/view.html', context={
        'boards': Board.objects.all(),
        'tops' : Card_top30.objects.all(),
        'current_card': Card.objects.get(id=card_id),
    })


def drop(request):
    payload = json.loads(request.body)
    card_title = str(payload.get('card_title'))
    column_id = int(payload.get('column_id'))
    assert card_title and column_id
    card = Card.objects.filter(title=card_title).order_by("-id")[0] #get(title=card_id)
    card.column = Column.objects.get(id=column_id)
    card.save()
    return HttpResponse()
