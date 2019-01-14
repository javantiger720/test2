# _*_ coding:utf-8 _*_
from django.db import models
from tinymce.models import HTMLField


class BookInfoManager(models.Manager):
    def get_query(self):
        return super(BookInfoManager, self).get_queryset().filter(bis_delete=False)


class BookInfo(models.Model):
    book1 = models.Manager()
    book2 = BookInfoManager()

    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    bis_delete = models.BooleanField(default=False)

    @classmethod
    def create(cls, title, pub_date):
        b = BookInfo()
        b.btitle = title
        b.bpub_date = pub_date
        b.bread = 0
        b.bcomment = 0
        b.bis_delete = False
        return b

    def __str__(self):
        return self.btitle

    class Meta:
        db_table = "bookinfo"


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    his_delete = models.BooleanField(default=False)
    book = models.ForeignKey('BookInfo', on_delete=True)

    @classmethod
    def create(cls, name, content, book=None):
        h = HeroInfo()
        h.hname = name
        h.hgender = True
        h.hcontent = content
        h.his_delete = False
        h.book = book
        return h

    def __str__(self):
        return self.hname


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', null=True, blank=True, on_delete=True)


class TinymceTest(models.Model):
    content = HTMLField()
