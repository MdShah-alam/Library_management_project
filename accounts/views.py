from django.shortcuts import render , redirect , HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from . forms import RegistrationForm , BookStoreForm
from . models import BookModel
# Create your views here.

def home(request):
    return render(request , 'home.html')

def singup(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                messages.success(request , 'Account created successfully ..........')
                print(form.cleaned_data)
        else:
            form=RegistrationForm()
        return render(request , 'singup.html' , {'form':form})
    else:
        return redirect('showpage')

def my_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request , data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name , password=userpass)
                if user is not None:
                    login(request , user)
                    return redirect('showpage')
        else:
            form=AuthenticationForm()
        return render(request , './login.html' , {'form':form})
    else:
        return redirect('showpage')

def my_logout(request):
    logout(request)
    return redirect('homepage')

def bookstore(request):
    if request.method == 'POST':
        data=BookStoreForm(request.POST)
        if data.is_valid():
            data.save(commit=True)
            print(data.cleaned_data)
            return redirect('showpage')
    else:
        data=BookStoreForm  
    return render(request , 'store_book.html' , {'data':data})

def bookshow(request):
    data = BookModel.objects.all()
    return render(request , 'show_book.html' , {'data':data})

def borrowbook(request , id):
    data = BookModel.objects.all()
    for bk in data:
        if bk.isbn==id:
            book=BookModel.objects.get(isbn = id)
            if book.count>1:
                book.count-=1
                book.save()
                print(bk.isbn , id , bk.count )
                return redirect('showpage')
            else:
                book=BookModel.objects.get(isbn = id).delete()
    return redirect('showpage')

def returnbook(request , id):
    data = BookModel.objects.all()
    for bk in data:
        if bk.isbn == id:
            book=BookModel.objects.get(isbn = id)
            book.count += 1
            book.save()
    return redirect('showpage')
            
