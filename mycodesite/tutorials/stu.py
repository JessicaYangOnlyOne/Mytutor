from django.shortcuts import render
from .models import User
from .models import Tutor
from .models import Student
from .models import Session
from .models import Review
from .models import wallet
import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def stu_search(request):
    return render(request,'tutorials/stu_search.html')

def stu_res_search(request):
    tutor_family_name= request.GET.get('tutor_family_name', None)
    tutor_given_name = request.GET.get('tutor_given_name', None)
    if tutor_family_name==None:
        res_user=Tutor.objects.filter(name__given_name__contains=tutor_given_name)
    elif tutor_given_name==None:
        res_user=Tutor.objects.filter(name__family_name__contains=tutor_family_name)
    else:
        res_user=Tutor.objects.filter(name__family_name__contains=tutor_family_name,name__given_name__contains=tutor_given_name)
    return render(request,'tutorials/stu_res_search.html',{'res_user':res_user})

def stu_tutor_info(request,row_username):
    res=Session.objects.filter(tutor_username__contains=row_username,stu_username="NULL")
    res_tutor=User.objects.filter(username__contains=row_username)
    request.session['tutor_name']=res_tutor[0].username
    #return HttpResponse("row_username="+row_username)
    return render(request,'tutorials/stu_tutor_info.html',{'res':res,'res_tutor':res_tutor})

def book_confirm(request,session_id):
    stu_username=request.session.get('username')
    tutor_name=request.session.get('tutor_name')
    res_session=Session.objects.get(pk=session_id)
    res_tutor=Tutor.objects.filter(name__username__contains=tutor_name)[0]
    res_stu=wallet.objects.filter(username=stu_username)[0]
    return render(request,'tutorials/stu_book_confirm.html', {'res_session':res_session,'res_tutor':res_tutor,'res_stu':res_stu,'session_id':session_id})

def book_success(request,session_id):
    stu_username=request.session['username']
    tutor_username=request.session.get('tutor_name')
    #add stu_username to session
    Session.objects.filter(pk=session_id).update(stu_username=stu_username)
    res_tutor = Tutor.objects.filter(name__username__contains=tutor_username)[0]
    res_wallet=wallet.objects.filter(username=stu_username)[0]
    bal=res_wallet.balance-res_tutor.hourly_rate
    #balance minus
    wallet.objects.filter(username=stu_username).update(balance=bal)
    return render(request,'tutorials/stu_book_success.html')

def view_book_session(request):
    stu_username=request.session['username']
    res_session=Session.objects.filter(stu_username__contains=stu_username)
    return render(request,'tutorials/stu_view_book_session.html',{"res_session":res_session})

def cancel_confirm(request,session_id):
    return render(request,'tutorials/stu_cancel_confirm.html',{'session_id':session_id})

def cancel_success(request,session_id):
    res_session=Session.objects.filter(pk=session_id)[0]
    res_tutor=Tutor.objects.filter(name__username__contains=res_session.tutor_username)[0]
    stu_username=request.session['username']
    res_wallet=wallet.objects.get(username=stu_username)
    bal=res_wallet.balance+res_tutor.hourly_rate
    wallet.objects.filter(username=stu_username).update(balance=bal)
    Session.objects.filter(pk=session_id).update(stu_username='NULL')
    return render(request,'tutorials/stu_cancel_success.html',{'bal':bal})






