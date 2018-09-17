#-*-coding:utf-8-*- 
#作者：zjq
#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    #获取网页输入内容
    user_text = request.GET['text']
    #创建一个字典
    word_dirt = {}
    #统计每个文字出现的次数
    for word in user_text:
        if word not in word_dirt:
            word_dirt[word] = 1  #第一次出现的字，记录为一
        else:
            word_dirt[word] += 1 #不是第一次出现的字加一
    #按照出现次数排序
    sort_word_dir = sorted(word_dirt.items(), key=lambda w: w[1],reverse=True)
    context = {"worddirt": sort_word_dir}
    return render(request, 'count.html', context)
