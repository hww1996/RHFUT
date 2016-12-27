#coding:utf-8
from django.contrib import admin
from lean.models import Category, Page
from lean.models import Article
from lean.models import Music
from lean.models import Qiang
from lean.models import UpArticle
from lean.models import Reporters
from lean.models import Program
from lean.models import photoupdata
from lean.models import play
from lean.models import Programcategory


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class ArticleAdimin(admin.ModelAdmin):
    list_disaplay=['title','timestamp']
#音乐
class MusicAdmin(admin.ModelAdmin):
    list_display = ['music_name', 'music_singer','music_number','time']
    list_filter=['time']

#墙区
class QiangAdmin(admin.ModelAdmin):
    list_display = ['title','name', 'author','time']
    list_filter=['name','time']
    search_fields=['name','author']

#文章投稿
class UpArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','time']
    list_filter=['time']

#主播
class ReportersAdmin(admin.ModelAdmin):
    list_display = ['category','name']
    list_filter=['category']

#节目
class ProgramAdimin(admin.ModelAdmin):
    list_disaplay=['category','title','timestamp']
    list_filter=['category','timestamp']

class photoupdataAdmin(admin.ModelAdmin):
    list_disaplay=['username','time']

class playAdmin(admin.ModelAdmin):
    list=['name',]

class ProgramcategoryAdmin(admin.ModelAdmin):
    list_display=['category',]



# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
#文章区
admin.site.register(Article,ArticleAdimin)
#音乐区
admin.site.register(Music, MusicAdmin)
#墙区
admin.site.register(Qiang,QiangAdmin)
#文章投稿区
admin.site.register(UpArticle,UpArticleAdmin)
#主播
admin.site.register(Reporters,ReportersAdmin)
#节目
admin.site.register(Program,ProgramAdimin)
#上传照片
admin.site.register(photoupdata,photoupdataAdmin)

admin.site.register(Programcategory,ProgramcategoryAdmin)


admin.site.register(play,playAdmin)