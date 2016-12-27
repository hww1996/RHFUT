import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

from lean.models import Category, Page


def populate():
    fengyu_cat = add_cat(name='Fenyu', age=20)

    add_page(cat=fengyu_cat,
        title="Smaetisan",
        url="http://www.smartisan.com/#/")

    
    yuqiuyang_cat = add_cat(name="Yuqiuyang", age=19)

    add_page(cat=yuqiuyang_cat,
        title="红茶有毒",
        url="http://yqy96.tk/")

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print ("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, age):
    c = Category.objects.get_or_create(name=name)[0]
    c.age=age
    c.save()
    return c

if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()