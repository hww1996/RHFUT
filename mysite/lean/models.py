#coding:utf-8
from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    age=models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

#这是文件上传的models
class photoupdata(models.Model):
    username = models.CharField('相片名字',max_length = 30,default='请输入相片的名字')
    usage=models.CharField('用于（周几的文章）',max_length=30,default='周一')
    time=models.DateTimeField()
    headImg = models.FileField(upload_to = './lean/static/program/')

    def __str__(self):
        return self.username
	
#这是文本上传
class Article(models.Model):
    title=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    content = RichTextField('正文')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-timestamp']

#这里是点歌的的models
MUSIC_NUMBER_CHOICES = (
    ('一首', '一首'),
    ('两首', '两首'),
    ('三首', '三首'),
    ('四首', '四首'),
    ('NO', 'NO'),
)
class Music(models.Model):
    music_name = models.CharField('歌名',max_length=100)
    music_singer=models.CharField('歌手',max_length=100)
    music_number = models.CharField('歌曲数量',max_length=2, choices=MUSIC_NUMBER_CHOICES)
    message=models.TextField('留言', max_length=280)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.music_name

#墙区的models
Type_choice=(
    ('吐槽','吐槽'),
    ('表白','表白'),
    ('失物','失物'),
    ('活动','活动'),
)

class Qiang(models.Model):
    name=models.CharField('类别',choices=Type_choice,blank=False,max_length=2)
    title=models.CharField('题目',max_length=50)
    author=models.CharField('作者',max_length=20,default='匿名')
    content=models.TextField('内容',max_length=280)
    time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-time']


#文章投稿
class UpArticle(models.Model):
    title=models.CharField('题目',max_length=100)
    author=models.CharField('作者',max_length=100,default='匿名')
    content=models.TextField('内容',max_length=6000)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

#主播
Type_choices=(
    ('中文主播','中文主播'),
    ('英文主播','英文主播'),
)

class Reporters(models.Model):
    category=models.CharField('类别',choices=Type_choices,blank=False,max_length=4)
    name=models.CharField('姓名',max_length=100,unique=True)
    timestamp = models.DateTimeField('创建时间')
    summary=models.CharField('主播总结',max_length=1000)
    headImg = models.FileField(upload_to = './lean/static/zhubo/')
    partner=models.CharField('搭档',max_length=100,unique=True)
    content = RichTextField('简介')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-timestamp']

#节目种类
class Programcategory(models.Model):
    category=models.CharField('类别',max_length=32)
    reporter=models.ManyToManyField(Reporters)
    def __str__(self):
        return self.category


#节目
class Program(models.Model):
    category=models.ManyToManyField(Programcategory)
    title=models.CharField('题目',max_length=100,unique=True)
    author=models.CharField('作者',max_length=50)
    reporter=models.ManyToManyField(Reporters)
    summary=models.CharField('简介',max_length=256)
    timestamp = models.DateTimeField('时间')
    content = RichTextField('内容')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-timestamp']


class play(models.Model):
    name=models.CharField(max_length=10)
    number1=models.IntegerField()
    number2=models.IntegerField()
    def __str__(self):
        return self.name