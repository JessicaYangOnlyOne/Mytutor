# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import User
from .models import Tutor
from .models import Student
from .models import Session
from .models import Review


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def welcome(request):
    return HttpResponse(request,)

def login(request):

    return

def homepage(request):
    return

def stu_search(request):
    return

def stu_res_search(request):
    return

def stu_tutor_info(request):
    return

def stu_book_confirm(request):
    return

def stu_book_success(request):
    return

#cancel
def stu_veiw_booksession(request):
    return

def stu_cancel_confirm(request):
    return

def stu_cancel_sign(request):
    return