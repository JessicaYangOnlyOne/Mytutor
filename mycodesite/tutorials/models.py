# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20,primary_key=True, default='NULL') #should be the primary key
    pass_word=models.CharField(max_length=20,default='NULL') #should not be seen by others & be masked by ******
    family_name=models.CharField(max_length=20,default='NULL')
    given_name=models.CharField(max_length=30,default='NULL')
    email=models.EmailField(default='NULL',blank=True)
    phone_num=models.CharField(max_length=15,default='NULL',blank=True)
    image=models.ImageField(upload_to='photos',blank=True) # save the self-image to photos
    def __str__(self):
        return self.username

class Student(models.Model):
    name = models.OneToOneField(User)
    interests=models.CharField(max_length=20,default='')
    def get_username(self):
        return self.name.username
    def get_family_name(self):
        return self.name.family_name
    def get_given_name(self):
        return self.name.given_name

class Tutor(models.Model):
    name=models.OneToOneField(User)
    #username = models.OneToOneField(User)
    hourly_rate=models.IntegerField(default=0)
    avg_review_score=models.FloatField(default=0,blank=True)
    short_profile=models.TextField(blank=True)
    university=models.CharField(max_length=50,blank=True)
    course_code=models.CharField(max_length=10,blank=True)
    contacted=models.BooleanField(blank=True)
    subjects_tags=models.CharField(max_length=10,blank=True)
    def get_username(self):
        return self.name.username
    def get_family_name(self):
        return self.name.family_name
    def get_given_name(self):
        return self.name.given_name

class Session(models.Model):
    #id = models.CharField(primary_key=True, unique_together=("tutor_username","start_time") #random number
    tutor_username=models.CharField(max_length=20,default="NULL")
    stu_username=models.CharField(max_length=20,default="NULL",blank=True)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    def get_tutor_username(self):
        return self.tutor_username

class Coupon_code(models.Model):
    coupon_code=models.CharField(max_length=30)

class wallet(models.Model):
    username=models.ForeignKey(User)
    balance=models.FloatField(default=0)
    def get_balance(self):
        return self.balance

class Review(models.Model):
    #id=models.CharField(max_length=22) #random number
    #stu_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    #tutor_name=models.ForeignKey(Tutor,on_delete=models.CASCADE)
    session_id=models.ForeignKey(Session,default='')
    review_score=models.IntegerField(default=0)
    review_text=models.TextField()
    #session=models.ForeignKey(Session)







