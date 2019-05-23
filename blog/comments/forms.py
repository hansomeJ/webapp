from article.models import Article
from comments.models import Comment
from django import forms

class CommentForm(forms.Form):
    name=forms.CharField(required=True,label='名字',widget=forms.TextInput(attrs={'id':'id_name','name':'name'}))
    email=forms.EmailField(required=True,label='邮箱',widget=forms.EmailInput(attrs={'id':'id_email','name':'email'}))
    url=forms.URLField(label='个人主页',widget=forms.URLInput(attrs={'id':'id_url','name':'url'}))
    comment=forms.CharField(required=True,label='内容',widget=forms.Textarea(attrs={'id':'id_comment','name':'comment'}))
