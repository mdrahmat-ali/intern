from django.shortcuts import render,redirect
from testapp.models import User,Artist,Work
from django.contrib.auth.decorators import login_required
from testapp.forms import RegisterForm

@login_required
def homeview(request):
    return render(request, 'home.html')

def userview(request):
    Users=User.objects.all()
    return render(request, 'user.html',{'Users':Users})

def artistview(request):
    Artists=Artist.objects.all()
    return render(request, 'arts.html',{'Artists':Artists})

def workview(request):
    Works=Work.objects.all()
    return render(request, 'works.html',{'Works':Works})

def thankview(request):
    return render(request,'thanku.html')

def registerview(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        form.save()
        return redirect('/accounts/login')
    return render(request, 'register.html',{'form':form})

