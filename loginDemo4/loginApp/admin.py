from django.contrib import admin

# Register your models here.
from loginApp.models import Event, Guest

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','start_time']
    search_fields = ['name']   #搜索框根据name匹配
    list_filter = ['status']   #过滤框根据status过滤

class GUestAdmin(admin.ModelAdmin):
    list_display = ['id','realname','phone','email','sign','create_time','event']
    search_fields = ['realname','phone']  #搜索框根据realname匹配或者phone匹配
    list_filter = ['sign']   #过滤框根据sign过滤

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GUestAdmin)