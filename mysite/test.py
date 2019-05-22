from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,reverse,redirect
import time
import random
def Time(fn):
    def inner(*args,**kwargs):
        time.process_time()
        fn(*args,**kwargs)
        print(time.process_time())
    return inner
@Time
def test1(n):
    list1=[]
    for i in range(n):
        x=random.randint(1,2*n)
        list1.append(x)
    list1.sort()
    for i in range(0,10):
        print(list1[i])
test1(1000000)