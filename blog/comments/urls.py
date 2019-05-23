from django.conf.urls import url
from . import views
app_name='comments'
urlpatterns = [
    url('add_comment/(\d+)/',views.add_comment.as_view(),name='add_comment'),
]