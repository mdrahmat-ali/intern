from django.shortcuts import render,redirect
from testapp.models import Client,Artist,Work
from django.contrib.auth.decorators import login_required
from testapp.forms import RegisterForm
from testapp.forms import ClientForm

@login_required
def homeview(request):
    return render(request, 'home.html')

def createview(request):
    form=ClientForm()
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/retrive')
    return render(request, 'create.html',{'form':form})

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

def retriveview(request):
    Clients=Client.objects.all()
    return render(request,'user.html',{'Clients':Clients})

def delete_view(request,id):
    client=Client.objects.get(id=id)
    client.delete()
    return redirect('/retrive')

def update_view(request,id):
    client=Client.objects.get(id=id)
    form=ClientForm(request.POST,instance=client)
    if form.is_valid():
        form.save()
        return redirect('/retrive')
    return render(request, 'update.html',{'client':client})

