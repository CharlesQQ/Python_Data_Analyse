from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class User(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    ut = models.ForeignKey(to='UserType',
                           to_field='id',
                           related_name='b',
                           limit_choices_to={'id__gt':5})   #如果这里是b，那么item.user_set.all()就变成item.b.all()
    #ut = models.ForeignKey(to='UserType',to_field='id',related_query_name='a')   #如果这里是b，那么item.user_set.all()就变成item.a_set.all()

class Blog(models.Model):
    slte = models.CharField(max_length=10)
    m = models.ManyToManyField('Tag',through='B2T',through_fields=['b','t'])

class Tag(models.Model):
    name = models.CharField(max_length=32)

class B2T(models.Model):
    b = models.ForeignKey('Blog')
    t = models.ForeignKey('Tag')
    status = models.IntegerField()

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

    def clean(self):
        from django.core.exceptions import ValidationError
        c = UserInfo.objects.filter(name=self.name).count()
        if c:
            raise ValidationError(message='用户名已经存在')


#正向查找
# v = User.objects.all()
# for item in v:
#     item.user
#     item.pwd
#
# User.objects.all().values('user','ut__name')
#

#反向查找
# v = UserType.objects.all()
# for item in v:
#     item.name
#     item.id
#     item.user_set.all()

# UserType.objects.all().values('name','user__pwd')

class UserType1(models.Model):
    caption = models.CharField(max_length=32)

    def __str__(self):
        return self.caption

class UserGroup(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class UserInfo1(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')   #verbosename会直接显示在前端(modelform)
    email = models.EmailField()
    user_type = models.ForeignKey('UserType1',to_field='id')
    u2g = models.ManyToManyField(UserGroup)

    def __str__(self):
        return self.username

class Category(models.Model):
    caption = models.CharField(max_length=16)


class ArticleType(models.Model):
    caption = models.CharField(max_length=16)

class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    article_type = models.ForeignKey(ArticleType)
    # type_chioce = (
    #     (1,'python'),
    #     (2,'openstack'),
    #     (3,'Linux'),
    # )
    # article_type_id = models.IntegerField(choices=type_chioce)