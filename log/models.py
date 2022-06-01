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

class LogTeacher(models.Model):
    #身分
    SET_OPTIONS = [
    (0, '社長'),
    (1, '社團指導教師'),
    (2, '教務處人員'),
    (3, '管理員'),
    ]
    #姓名
    subject_teacher = models.CharField('姓名', max_length=10)
    #身分
    status_teacher = models.IntegerField(
              '身分', 
              default=0, 
              choices=SET_OPTIONS
           )
    #社團
    clubdate = models.CharField('社團', max_length=10)


class LogClub(models.Model):
    #社團
    club = models.CharField('社團名稱', max_length=10)
    #社團指導老師
    club_teacher = models.CharField('指導老師', max_length=10)
    #社團上限人數
    club_person = models.CharField('社團上限人數', max_length=10)
    #社團目前人數
    club_now_person = models.CharField('社團目前人數', max_length=10)

    


    



