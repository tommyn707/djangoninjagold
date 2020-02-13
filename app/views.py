from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    if 'act_log' not in request.session:
        request.session['act_log'] = []

    return render(request, 'ninja_gold.html')

def get_gold(request):

    if request.POST['button'] == 'farm':
        mine = random.randrange(1,3)
        if mine == 1:
            goldval = random.randrange(1,9)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'>You've earned %s gold  (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session["gold_count"] += goldval
        if mine == 2:
            goldval = random.randrange(1,9)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'>No rain this season, %s gold  (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session['gold_count'] -= goldval

    if request.POST['button'] == 'cave':
        mine = random.randrange(1,3)
        if mine == 1:
            goldval = random.randrange(0,11)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'>  Found %s gold!  (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session["gold_count"] += goldval
        if mine == 2:
            goldval = random.randrange(1,11)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'>Lost %s gold (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session['gold_count'] -= goldval

    if request.POST['button'] == 'loot':
        mine = random.randrange(1,3)
        if mine == 1:
            goldval = random.randrange(2,6)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'>You found %s gold (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session["gold_count"] += goldval
        if mine == 2:
            goldval = random.randrange(2,5)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'>You lose %s gold (%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session['gold_count'] -= goldval

    if request.POST['button'] == 'casino':
        mine = random.randrange(1,3)
        if mine == 1:
            goldval = random.randrange(10,101)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log = "<p class='greentext'>Won %s gold from the casino!(%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session["gold_count"] += goldval
        if mine == 2:
            goldval = random.randrange(10,101)
            now = datetime.datetime.now()
            timestamp = now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> House wins! %s(%s)</p>" %(str(goldval),timestamp)
            temp = request.session['act_log']
            temp.insert(0,event_log)
            request.session['act_log'] = temp
            request.session['gold_count'] -= goldval

    return redirect('/')

def restart_game(request):
    request.session.clear()
    return redirect('/')

    