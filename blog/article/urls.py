from django.conf.urls import url, include
from . import views
from . import feed

app_name = 'article'
urlpatterns = [
    url('detail/(\d+)/', views.detail, name='detail'),
    url('tag/(\d+)/', views.tag, name='tag'),
    url('archive/(\d+)/(\d+)/', views.archive, name='archive'),
    url('category/(\d+)/', views.category, name='category'),
    url('rss/', feed.BlogFeed(), name='rss'),
    url('contact/', views.contact, name='contact'),
    url('addimg/', views.Add.as_view(), name='addimg'),
    url('^$', views.index, name='index'),

]
