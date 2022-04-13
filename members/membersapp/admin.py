from django.contrib import admin
from membersapp.models import member
# Register your models here.


# 加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
class memberAdmin(admin.ModelAdmin):
    list_display=('id','Name','Sex','Birthday','Email','Phone','Addr',)
    list_filter=('Name','Sex',)
    search_fields=('Name',)
    ordering=('id',)
admin.site.register(member,memberAdmin)
