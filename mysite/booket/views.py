from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from .models import Book,Hero
# Create your views here.

# 首页
def index(request):
    books=Book.objects.all()
    return render(request,'booket/index.html',{'books':books})

# 验证书名
@csrf_exempt
@require_GET
def book_name(request):
    book_name=request.GET['book_name'].strip()
    if len(book_name)==0:
        return JsonResponse({'isempty':True})
    try:
        book=Book.objects.get(book_name=book_name)
        return JsonResponse({'isexists':True})
    except Exception as e:
        print('捕获异常信息：',e)
        return JsonResponse({'issuccess':True})
# 验证作者
@csrf_exempt
@require_GET
def author(request):
    author=request.GET['author'].strip()
    if len(author)==0:
        return  JsonResponse({'issuccess':False})
    else:
        return JsonResponse({'issuccess':True})
#类型
@csrf_exempt
@require_GET
def type(request):
    type=request.GET['type'].strip()
    if len(type)==0:
        return JsonResponse({'issuccess':False})
    else:
        return JsonResponse({'issuccess':True})

#添加书籍
@csrf_exempt
@require_POST
def add(request):
    book_name=request.POST['book_name'].strip()
    author=request.POST['author'].strip()
    type=request.POST['type'].strip()
    book=Book(book_name=book_name,author=author,type=type)
    try:
        book.save()
        return JsonResponse({'issuccess':True})
    except Exception as e:
        print('捕获错误信息：',e)
        return JsonResponse({'issuccess': False})
def detail(request,b_id):
    book=Book.objects.get(pk=b_id)
    heros=book.hero_set.all()
    print(heros)
    return render(request,'booket/bookdetail.html',{"book":book,"heros":heros})
#修改书籍
@csrf_exempt
@require_POST
def update(request):
    book = Book.objects.get(pk=request.POST['id'].strip())
    book.book_name=request.POST['book_name'].strip()
    book.author=request.POST['author'].strip()
    book.type=request.POST['type'].strip()
    print(book)
    try:
        book.save()
        return JsonResponse({'issuccess':True})
    except Exception as e:
        print('捕获错误信息：',e)
        return JsonResponse({'issuccess': False})

def add_hero(request,b_id):
    book=Book.objects.get(pk=b_id)
    if request.method=='GET':
        return render(request,'booket/add_hero.html',{"book":book})
    else:
        hero_name=request.POST['hero_name']
        gender=request.POST['gender']
        skill=request.POST['skill']

        hero=Hero(hero_name=hero_name,gender=gender,skill=skill,book=book)
        try:
            hero.save()
            return redirect(reverse('booket:detail' ,kwargs={'b_id':b_id} ))
        except Exception as  e:
            print(e)
            return render(request,'booket/add_hero.html',{"book":book})

def hero_detail(request,h_id):
    hero=Hero.objects.get(pk=h_id)
    return render(request,'booket/herodetail.html',{'hero':hero})