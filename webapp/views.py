from django.shortcuts import render , redirect

from .forms import CreateUserform , LoginForm , CreateRecordForm , UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Record
# Create your views here.

# Home page
def home(request):
    return render(request,"webapp/index.html")


# Register view

def register(request):
    
    form = CreateUserform()
    
    if request.method == "POST":
        
        form = CreateUserform(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request,"Your account is successfully created!!!")
            
            return redirect("my-login")
            
    context = {"form":form}
    
    return render(request,"webapp/register.html",context=context)



def my_login(request):
    
    form = LoginForm()
    
    if request.method == "POST":
        
        form = LoginForm(request,data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authenticate(request,username=username,password=password)
            
            # process below is user exists
            
            if user is not None:
                auth.login(request,user)
                
                messages.success(request,"You logged in successfully")
                
                return redirect("dashboard")
            
    context = {"form":form}
    return render(request,"webapp/my-login.html",context=context)
            
        

# Dashboard 
@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()
    messages.success(request,"You are on home page ")
    context = {"records":my_records}
    return render(request,"webapp/dashboard.html",context)
        
        

@login_required(login_url="my-login")
def create_record(request):
    
    # Below instance of a class is only for diaplay the form
    form = CreateRecordForm()
    
    
    # Below all functionality is for backend process of form 
    if request.method == "POST":
        
        form = CreateRecordForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,"You record is successfully created!!!")
            return redirect("dashboard")
        
    context = {"form":form}
    return render(request,"webapp/create-record.html",context=context)
        
@login_required(login_url="my-login")
def update_recors(request,pk):
    
    # Get the objects by id which is reffered by primarykey
    record = Record.objects.get(id=pk)
    
    form = UpdateRecordForm(instance=record)
    
    if request.method == "POST":
        form = UpdateRecordForm(request.POST,instance=record)
        
        if form.is_valid():
            form.save()
            messages.success(request,"Your record is successfully updated!!!")
            return redirect("dashboard")
    context = {"form":form}
    return render(request,"webapp/update-record.html",context=context)
    
    

# Read a singular record

@login_required(login_url="my-login")
def singular_record(request,pk):
    all_record = Record.objects.get(id=pk)
    
    context = {"record":all_record}
    
    return render(request,"webapp/view-record.html",context=context)


@login_required(login_url="my-login")
def delete_record(request,pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request,"your record successfully deleted!!!")
    return redirect("dashboard")    
        
        
def user_logout(request):
    auth.logout(request)
    messages.success(request,"logout successessfully!!!")
    return redirect("my-login")

