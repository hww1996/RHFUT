#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render,render_to_response
from django import forms
from lean.models import Page
from lean.models import Category
from lean.models import photoupdata
from lean.models import Article
from lean.models import Music
from lean.models import Qiang
from lean.models import UpArticle
from lean.models import Reporters
from lean.models import Program
from lean.forms import MusicForm
from lean.forms import QiangForm
from lean.forms import UpArticleForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
from lean.models import play
from lean.models import Programcategory

def index(request):
    category_list = Category.objects.order_by('-age')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'index.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'category.html', context_dict)

def dajia(request):
    return render(request,'dajia.html')

#这是文件上传的views
class photoupdataForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

def register(request):
    if request.method == "POST":
        uf = photoupdataForm(request.POST,request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            user = User()
            user.username = username
            user.headImg = headImg
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = photoupdataForm()
    return render_to_response('register.html',{'uf':uf})

#这是后台文章
def blog(request,article_content):
    context_dict={}
    try:
        article=Article.objects.get(title=article_content)
        context_dict['article_content']= article.content
        context_dict['article']=article
    except Article.DoesNotExist:
        pass
    return render(request, 'blog.html', context_dict)

#文章区views
def wen(request):
    article=Article.objects.all()
    return render_to_response('wenzhang.html',{'article':article})

def shi(request):
    article=Article.objects.all()
    return render_to_response('try.html',{'article':article})

#这是音乐上传的views
def music(request):
    if request.method == 'POST':
        form =MusicForm(request.POST)
        if form.is_valid():
            music_info = form.save()
            music_info.save()
            return HttpResponse('音乐信息上传成功，+1s')
    else:
        form = MusicForm()
    return render(request, 'music.html', {'form_info': form})

#首页
def shouye(request):
    qiang=Qiang.objects.all()
    paginator = Paginator(qiang, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'contacts': contacts})


#墙区的views
def fatie(request):
    if request.method == 'POST':
        form =QiangForm(request.POST)
        if form.is_valid():
            qiang_info = form.save()
            qiang_info.save()
            return HttpResponseRedirect('/qiang/')
    else:
        form =QiangForm()
    return render(request, 'fatie.html', {'form_info': form})

def detail(request,qiang_id):
    qiang=Qiang.objects.get(id=qiang_id)
    return render_to_response('detail.html',{'qiang_detail':qiang})


def qiang(request):
    qiang=Qiang.objects.all()
    paginator = Paginator(qiang, 9) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'qiang.html', {'contacts': contacts})




def shiwu(request):
    qiang=Qiang.objects.filter(name='失物')
    paginator = Paginator(qiang, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'qiang.html', {'contacts': contacts})


def tucao(request):
    qiang=Qiang.objects.filter(name='吐槽')
    paginator = Paginator(qiang, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'qiang.html', {'contacts': contacts})

def biaobai(request):
    qiang=Qiang.objects.filter(name='表白')
    paginator = Paginator(qiang, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'qiang.html', {'contacts': contacts})

def huodong(request):
    qiang=Qiang.objects.filter(name='活动')
    paginator = Paginator(qiang, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'qiang.html', {'contacts': contacts})

#文章投稿
def uparticle(request):
    if request.method == 'POST':
        form =UpArticleForm(request.POST)
        if form.is_valid():
            uparticle_info = form.save()
            uparticle_info.save()
            return HttpResponse('文章上传成功,你将和华莱士谈笑风生')
    else:
        form = UpArticleForm()
    return render(request, 'uparticle.html', {'form_info': form})

#主播
def reporter(request,reporter_content):
    context_dict={}
    try:
        reporter=Reporters.objects.get(name=reporter_content)
        context_dict['reporter_name']=reporter.name
        context_dict['reporter_content']= reporter.content
        context_dict['reporter_partner']=reporter.partner
        program=reporter.program_set.all()
        paginator = Paginator(program, 5) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        context_dict['reporter_program']=contacts
    except Reporters.DoesNotExist:
        pass
    return render(request, 'reporter.html', context_dict)

#主播更多
def reporter_program(request,reporter_content):
    context_dict={}
    try:
        reporter=Reporters.objects.get(name=reporter_content)
        context_dict['reporter_name']=reporter.name
        program=reporter.program_set.all()
        paginator = Paginator(program, 5) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        context_dict['reporter_program']=contacts
    except Reporters.DoesNotExist:
        pass
    return render(request, 'reporter_program.html', context_dict)

#主播总览
def zhubo(request):
    zhongreporter=Reporters.objects.filter(category='中文主播')
    paginators = Paginator(zhongreporter, 2) # Show 25 contacts per page
    pages = request.GET.get('page')
    try:
        contacts = paginators.page(pages)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginators.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginators.page(paginators.num_pages)
    yingreporter=Reporters.objects.filter(category='英文主播')
    paginator = Paginator(yingreporter, 2) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contact = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contact = paginator.page(paginator.num_pages)
    return render_to_response('zhubo.html',{'contacts': contacts,'contact': contact})
#中文
def chinese(request):
    zhongreporter=Reporters.objects.filter(category='中文主播')
    paginator = Paginator(zhongreporter, 2) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'chinese.html',{'contacts': contacts})
#英文
def english(request):
    yingreporter=Reporters.objects.filter(category='英文主播')
    paginator = Paginator(yingreporter, 2) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'english.html',{'contacts': contacts})

#节目总列表
def jiemu(request):
    jiemu=Program.objects.all()
    paginator = Paginator(jiemu, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    category=Programcategory.objects.all()
    return render(request,'jiemu.html',{'contacts': contacts,'category':category})
'''#周一
def mon(request):
    zhouyi=Program.objects.filter(category='周一')
    paginator = Paginator(zhouyi, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'jiemu.html',{'contacts': contacts})
#周二
def tue(request):
    zhouer=Program.objects.filter(category='周二')
    paginator = Paginator(zhouer, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'jiemu.html',{'contacts': contacts})
#周三
def wed(request):
    zhousan=Program.objects.filter(category='周三')
    paginator = Paginator(zhousan, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'jiemu.html',{'contacts': contacts})
#周四
def thu(request):
    zhousi=Program.objects.filter(category='周四')
    paginator = Paginator(zhousi, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'jiemu.html',{'contacts': contacts})
#周五
def fir(request):
    zhouwu=Program.objects.filter(category='周五')
    paginator = Paginator(zhouwu, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'jiemu.html',{'contacts': contacts})
#早间播音
def zaojian(request):
    zaojian=Program.objects.filter(category='早间节目')
    paginator = Paginator(zaojian, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'jiemu.html',{'contacts': contacts})'''

#节目分类
def program_list(request,program_categories):
    context_dict={}
    try:
        category=Programcategory.objects.get(category=program_categories)
        program=category.program_set.all()
        paginator = Paginator(program, 5) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        context_dict['contacts']= contacts
        context_dict['category']=Programcategory.objects.all()
        context_dict['category_name']=category.category
    except Programcategory.DoesNotExist:
        pass
    return render(request, 'program_list.html', context_dict)






#节目后台
def program(request,program_content):
    context_dict={}
    try:
        program=Program.objects.get(title=program_content)
        context_dict['program_title']= program.title
        context_dict['program_timestamp']= program.timestamp
        context_dict['program_content']= program.content
        context_dict['program_reporter']=program.reporter.all()
    except Program.DoesNotExist:
        pass
    return render(request, 'program.html', context_dict)

#加入我们
def jiaru(request):
    return render(request,'jiaru.html')
#关于
def guanyu(request):
    return render(request,'guanyu.html')

def playing(request):
    dic={'sum':[]}
    j=0
    k=0
    try:
        fuck=play.objects.all()
        dic['name']=[]
        dic['number1']=[]
        dic['number2']=[]
        for i in fuck:
            j=i.number1
            k=i.number2
            dic['sum'].append(str(int(j)+int(k)))
            dic['name'].append(i.name)
            dic['number1'].append(i.number1)
            dic['number2'].append(i.number2)
    except play.DoesNotExist:
        pass
    return render_to_response('play.html',dic)

