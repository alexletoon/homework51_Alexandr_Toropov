from random import randint
from django.shortcuts import render

from .cat_db import Database



class Cat():

    def add_cat(self, request):
        Database.cat['cat_name']=request.POST.get('cat_name')
        Database.cat['cat_age'] = 2
        Database.cat['cat_health'] = 80
        Database.cat['cat_mood'] = 60
        Database.cat['cat_satiety'] = 60


    def feed_cat(self):
        if Database.cat['cat_satiety'] >= 100:
            Database.cat['cat_satiety'] = Database.cat['cat_satiety'] - 30
            Database.cat['cat_mood'] = Database.cat['cat_mood'] - 30
        if Database.cat['cat_mood'] >= 100:
            Database.cat['cat_satiety'] = Database.cat['cat_satiety'] - 30
            Database.cat['cat_mood'] = Database.cat['cat_mood'] - 30
        else:
            Database.cat['cat_mood'] = 100 if Database.cat['cat_mood'] + 7 >= 100 else Database.cat['cat_mood'] + 7
            Database.cat['cat_satiety'] = 100 if Database.cat['cat_satiety'] + 7 >=100 else Database.cat['cat_satiety']+7


    def play_cat(self):
        Database.cat['cat_mood'] = 100 if Database.cat['cat_mood'] + 7 >= 100 else Database.cat['cat_mood'] + 7
        Database.cat['cat_satiety'] = Database.cat['cat_satiety'] - 7


    def display_cat_img(self):
        if Database.cat['cat_mood'] >= 70 and Database.cat['cat_mood']<= 80:
            Database.cat['cat_img'] = Database.cat_img[1]
        elif Database.cat['cat_mood'] > 80:
            Database.cat['cat_img'] = Database.cat_img[2]
        elif Database.cat['cat_mood'] < 70:
            Database.cat['cat_img'] = Database.cat_img[0]
