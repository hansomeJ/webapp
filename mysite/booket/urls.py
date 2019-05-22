from django.urls import path
from django.conf.urls import url
from . import views
app_name='booket'
urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^book_name/',views.book_name,name='book_name'),
    url(r'^author/',views.author,name='author'),
    url(r'^type/',views.type,name='type'),
    url(r'^add/',views.add,name='add'),
    url(r'^detail/(?P<b_id>\d+)/',views.detail,name='detail'),
    url(r'^hero_detail/(?P<h_id>\d+)/',views.hero_detail,name='hero_detail'),
    url(r'^add_hero/(?P<b_id>\d+)/',views.add_hero,name='add_hero'),
    url(r'^update/',views.update,name='update'),
    # url(r'^test/',Test.Views(),name='uprdate'),
]