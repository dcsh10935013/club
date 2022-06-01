from django.db import models
from django.db.models.fields import DateField
from datetime import date
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    studata = models.TextField('學生資料', help_text='依 班級,座號,學號,身分證字號,姓名 順序由 Excel 貼上學生基本資料')

class LogItem(models.Model):
    student = models.CharField('',max_length=255)

class LogStudent(models.Model):
    SETTING_OPTIONS = [
    (0, '高一'),
    (1, '高二'),
    ]
    CLASS_OPTIONS = [
    (0, '1'),
    (1, '2'),
    (2, '3'),
    (3, '4'),
    (4, '5'),
    (5, '6'),
    (6, '7'),
    (7, '8'),
    (8, '9'),
    (9, '10'),
    ] 
    #學生姓名
    subject = models.CharField('學生姓名', max_length=10)
    #學生年級
    status = models.IntegerField(
              '年級', 
              default=0, 
              choices=SETTING_OPTIONS
           )
    #學生班級
    classnumber = models.IntegerField(
              '學生班級', 
              default=0, 
              choices=CLASS_OPTIONS
           )

    #學生原社團
    oldclub = models.CharField('原社團', max_length=10)
    #學生新社團
    newclub = models.CharField('原社團', max_length=10)




