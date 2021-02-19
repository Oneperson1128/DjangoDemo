from django.db import models

# Create your models here.

'''
默认生成自增id，不需要声明该字段
'''
class Event(models.Model):
    name = models.CharField(max_length=100)  #发布会标题
    limit = models.IntegerField() #参加人数
    status = models.BooleanField()  #状态，表示该发布会是否启用
    address = models.CharField(max_length=200)  #发布会地址
    start_time = models.DateTimeField('events time')  #发布会开始时间
    create_time = models.DateTimeField(auto_now=True)  #创建时间，自动获取当前时间

    '''
    python 如何将对象以str的方式显示出来
    '''
    def __str__(self):
        return self.name


class Guest(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)   #关联发布会id
    realname =models.CharField(max_length=64)  #来宾姓名
    phone = models.CharField(max_length=16)  #手机号
    email =models.EmailField() #邮箱
    sign = models.BooleanField()  #签到状态
    create_time = models.DateTimeField(auto_now=True)  #创建时间，自动获取当前时间

    class Meta:
        unique_together = ('event','phone')

    def __str__(self):
        return self.realname