from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User

# Create your views here.


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password1=request.POST['password1']
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid details')
            return redirect('login')
    else:
        messages.info(request,"USER DOESN'T EXISTS")
        return render(request,'login.html')



def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'USER ALREADY EXISTS')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                  messages.info(request,'EMAIL ALREADY EXISTS')
                  return  redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('USER CREATED')
        else:
            print('PASSWORD IS NOT MATCHED')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
    
        
  

def logout(request):
    auth.logout(request)
    return redirect('/')


