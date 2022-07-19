import datetime
from django.utils import timezone
from django.db import models

class AllCources(models.Model):
    courcename=models.CharField(max_length=100)
    instructorname=models.CharField(max_length=100)
    startedfrom=models.DateTimeField('Started From')
    def __str__(self):
        return self.courcename
    def was_published(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.startedfrom<=now

class details(models.Model):
    cources=models.ForeignKey(AllCources,on_delete=models.CASCADE)
    courcetype=models.CharField(max_length=200)
    choice=models.BooleanField(default=False)
    def __str__(self):
        return str(self.courcetype)

class students(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    coursename=models.CharField(max_length=100,null=True)
    stu_id=models.IntegerField()

    def __str__(self):
        return self.firstname
