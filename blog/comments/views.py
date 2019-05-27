from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import View
from comments.forms import CommentForm
from article.models import Article
from comments.models import Comment
# Create your views here.

class add_comment(View):
    def post(self,request,id):
        cf = CommentForm(request.POST)
        if cf.is_valid():
            article=get_object_or_404(Article, pk=id)
            username=cf.cleaned_data['name']
            # email=cf.changed_data['email']
            email=request.POST.get('email')
            url=request.POST.get('url')
            # url=cf.changed_data['url']
            # comment=cf.changed_data['comment']
            comment = request.POST.get('comment')
            c=Comment()
            c.username=username
            c.url=url
            c.article=article
            c.email=email
            c.content=comment
            c.save()
            return redirect(reverse('article:detail',args=(id,)))
        else:
            return redirect(reverse('article:detail',args=(id,)))


