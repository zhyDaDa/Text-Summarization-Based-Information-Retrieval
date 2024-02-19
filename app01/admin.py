from django.contrib import admin
admin.site.site_header = '电子病历信息检索管理后台'
from django.contrib import admin
from .models import User,medical


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_password')
    list_display_links=('user_id', 'user_name', 'user_password')
    actions_on_top =True
    actions_on_bottom = True
    actions_selection_counter = True
    empty_value_display = ' -空白- '
    # 过滤器功能及能过滤的字段
    list_filter = ('user_id', 'user_name')  
    # 搜索功能及能实现搜索的字段
    search_fields = ('user_id', 'user_name', ) 

class medicalAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_content', 'answer_content','question_extraction')
    list_display_links=('id', 'question_content', 'answer_content','question_extraction')
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top =True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # 过滤器功能及能过滤的字段
    list_filter = ('id', 'question_content')  
    # 搜索功能及能实现搜索的字段
    search_fields = ('id', 'question_content' ) 
admin.site.register(User,UserAdmin)
admin.site.register(medical,medicalAdmin)

