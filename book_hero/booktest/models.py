from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class BookInfoManager(models.Manager):

    # def del_queryset(self):
    #     self.model.isDelete = True

    def get_queryset(self):  # BookInfo.books.all()  等价于  BookInfo.books.get_queryset()
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    # 管理BookInfo类对象方法一： 需要save()函数进行提交数据库
    # def create_book(self, title, pub_date):
    #     book = self.model
    #     book.btitle = title
    #     book.bpub_data = pub_date
    #     book.bread = 0
    #     book.bcommnet = 0
    #     book.isDelete = False
    #     return book

    # 管理BookInfo类对象方法二： 调用self.create进行创建并保存对象，不需要手动save()
    def create_book(self, title, pub_date):
        book = self.create(btitle=title, bpub_data=pub_date, bread=0, bcommnet=0, isDelete=False)
        return book


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_data = models.DateTimeField()  # 图书发布时间
    bread = models.IntegerField(default=0)
    bcommnet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    content = HTMLField(verbose_name='文章详情', default='test')
    books = BookInfoManager()

    def __str__(self):
        return '图书名称： {}, 发布时间： {}, bread： {}, bcomment： {}'.format(self.btitle, self.bpub_data.strftime('%Y-%m-%d'),
                                                                    self.bread, self.bcommnet)

    def hero_name(self):
        return self.btitle

    class Meta:
        ordering = ['id']


class HeroInfoManager(models.Manager):
    def get_queryset(self):
        return super(HeroInfoManager, self).get_queryset().filter(isDelete=False)

    def create_hero(self, hname, hgender, hcontent):
        hero = self.create(hname=hname, hgender=True, hcontent=hcontent, isDelete=False)
        return hero


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄姓名
    hgender = models.BooleanField(default=True)  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 是否已被删除
    hcontent = models.CharField(max_length=100)  # 英雄简介
    hbook = models.ForeignKey(BookInfo, on_delete=models.SET_NULL, null=True)  # 所属图书
    heros = HeroInfoManager()

    # 关系为一对多

    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    def sho_name(self):
        return self.hname

    def __str__(self):

        return '英雄姓名： {}, 英雄性别： {}, 英雄简介： {}, 关联关系： {}' \
            .format(self.hname, self.gender(), self.hcontent, self.hbook)

    class Meta:
        ordering = ['id']


# id, provinceid, province
# 1,   110000,    '北京市'
# provinces
class ProvInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    provinceid = models.CharField(max_length=10, unique=True)
    province = models.CharField(max_length=20)
    content = HTMLField(verbose_name='文章详情', default='test')

    class Meta:
        db_table = 'provinces'

    def __str__(self):
        return {'id': self.id,
                'provinceid': self.provinceid,
                'province': self.province}


# id, cityid, city, provinceid
# 1,'110100','北京市','110000'
# cities
# course = models.ForeignKey(CourseInfo, to_field="course_id")  使用to_field字段指定外键字段名
class CityInfo(models.Model):  # 城市数据库类
    id = models.IntegerField(primary_key=True)
    cityid = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    province = models.ForeignKey(ProvInfo, on_delete=models.SET_NULL, to_field='provinceid', null=True)

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return {'id': self.id,
                'cityid': self.cityid,
                'city': self.city
                }


# id  areaid  area  cityid
# 1,'110101','东城区','110100'
# areas
class AreaInfo(models.Model):  # 区县数据库类
    id = models.IntegerField(primary_key=True)
    areaid = models.CharField(max_length=10)
    area = models.CharField(max_length=100)

    city = models.ForeignKey(CityInfo, on_delete=models.SET_NULL, to_field='cityid', null=True)

    class Meta:
        db_table = 'areas'

    def __str__(self):
        return {'id': self.id,
                'areaid': self.areaid,
                'area': self.city
                }

"""
    建立外键报错：
    
（1）外键对应的字段数据类型不一致

（2）两张表的存储引擎不一致

（3）设置外键时“删除时”设置为“SET NULL”

     于是，我利用排除法，首先查看表的存储引擎，发现都是InnoDB引擎，
     排除第二条；设置外键时“删除时”设置为“SET NULL”，
     我改为其他的选项，发现也不能保存，故排除了第三项；接着，我查看了外键对应的字段的数据类型，发现它们竟然不一致
"""
