from django.contrib import admin
from .models import Tag,Article,Category,MessageInfo,Ads
# Register your models here.

admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(MessageInfo)
admin.site.register(Ads)

