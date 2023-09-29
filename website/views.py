from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomer
from .models import Customer


# Create your views here.
def home(request):
    customers = Customer.objects.all()
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'website/home.html', {"customers":customers})
    

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Successfully Registered!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'website/register.html', {'form': form})
    return render(request, 'website/register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        return render(request, 
                      "website/customer_record.html", 
                      {"cust_record": customer_record})
    else:
        messages.success(request, 'You Must Be Logged In To That Page!')
        return redirect('home')
    
# Delete a customer by thier id
def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_record = Customer.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Customer Record Deleted Successfully!")
        return redirect('home')
    else:
        messages.success(request,"You Must Be Logged In To That Page!")
        return redirect('home')
    
    
# Add a customer
def add_customer(request):
    form = AddCustomer(request.POST or None)
    if  request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_customer = form.save()
                messages.success(request, "Customer Add")
                return redirect('home')
        return render(request, 'website/add_customer.html',{'form':form})
    else:
        messages.success(request,"You Must Be Logged In To That Page!")
        return redirect('home')
        
def update_customer(request, pk):
    if request.user.is_authenticated:
        current_customer = Customer.objects.get(id=pk)
        form = AddCustomer(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request,"Customer Has Been Updated!")
            return redirect('home')
        else:
            return render(request, 'website/update_customer.html',{'form':form})
    else:
        messages.success(request,"You Must Be Logged In To That Page!")
        return redirect('home')