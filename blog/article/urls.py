from django.conf.urls import url,include
from . import views
app_name='article'
urlpatterns = [
    url('^$',views.index,name='index'),
    url('detail/(\d+)/',views.detail,name='detail'),
]