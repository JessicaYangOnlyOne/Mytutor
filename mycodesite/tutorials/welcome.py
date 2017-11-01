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

def welcome(request):
    return render(request,'tutorials/welcome.html')

def login(request):
    request.session['username'] = None
    return render(request,'tutorials/login.html')

def signup(request):
    return render(request,'tutorials/signup.html')

def homepage(request):
    if request.session['username'] == None:
        username = request.GET.get('username', None)
        pass_word = request.GET.get('pass_word', None)
        request.session['username'] = username
        # return HttpResponse("username="+username)
        res = User.objects.filter(username=username, pass_word=pass_word)
        if res == None:
            return render(request, 'tutorials/welcome.html')
        else:
            res_wallet = wallet.objects.filter(username=request.session['username'])[0]
            return render(request, 'tutorials/homepage.html', {'res_wallet': res_wallet})
    else:
        res_wallet=wallet.objects.filter(username=request.session['username'])[0]
        return render(request,'tutorials/homepage.html',{'res_wallet':res_wallet})
#
