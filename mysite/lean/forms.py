#coding:utf-8
from django.forms import ModelForm
from lean.models import Music
from lean.models import Qiang
from lean.models import UpArticle
#音乐区表单
class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = '__all__'
#墙区表单
class QiangForm(ModelForm):
    class Meta:
        model=Qiang
        fields='__all__'

#文章投稿
class UpArticleForm(ModelForm):
    class Meta:
        model=UpArticle
        fields='__all__'