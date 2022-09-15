from django.shortcuts import render, redirect

from .cat_db import Database
from .cat import Cat



def add_cat_view(request):
    if request.method == 'GET':
        return render(request, 'add_cat.html')
    print(request.POST.get('cat_name'))
    Cat().add_cat(request)
    return redirect('/cat_stats/')


def cat_stats_view(request):
    if request.POST.get('action')=='feed':
        cat = Database.cat
        Cat().feed_cat()
        Cat().display_cat_img()
        print(cat.get('cat_img'))
        return render (request, 'cat_stats.html', context={
            'cat_name': cat.get('cat_name'),
            'cat_age': cat.get('cat_age'),
            'cat_health': cat.get('cat_health'),
            'cat_mood': cat.get('cat_mood'),
            'cat_satiety': cat.get('cat_satiety'),
            'cat_img': cat.get('cat_img')
        })
    elif request.POST.get('action')=='play':
        cat = Database.cat
        Cat().play_cat()
        Cat().display_cat_img()
        print(cat.get('cat_img'))
        return render (request, 'cat_stats.html', context={
            'cat_name': cat.get('cat_name'),
            'cat_age': cat.get('cat_age'),
            'cat_health': cat.get('cat_health'),
            'cat_mood': cat.get('cat_mood'),
            'cat_satiety': cat.get('cat_satiety'),
            'cat_img': cat.get('cat_img')
        })
    Cat().add_cat(request)
    cat = Database.cat
    Cat().display_cat_img()
    print(cat.get('cat_img'))
    return render (request, 'cat_stats.html', context={
        'cat_name': cat.get('cat_name'),
        'cat_age': cat.get('cat_age'),
        'cat_health': cat.get('cat_health'),
        'cat_mood': cat.get('cat_mood'),
        'cat_satiety': cat.get('cat_satiety'),
        'cat_img': cat.get('cat_img')
    })


