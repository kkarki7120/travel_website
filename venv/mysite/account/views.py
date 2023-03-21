from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, GuideSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from product.models import *



from product.models import *


def index(request):
    newest_products = Product.objects.all()[0:8]

    return render(request, '../templates/index.html', {'newest_products': newest_products})

def register(request):
    return render(request, '../templates/register.html')

def gallery(request):
    return render(request, '../templates/gallery.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
       
        return redirect('login')

class guide_register(CreateView):
    model = User
    form_class = GuideSignUpForm
    template_name = '../templates/guide_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_customer:
                login(request, user)
                return redirect('/')
            elif user is not None and user.is_guide:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')





def customer(request):
    return render(request,'customer.html')


def add_product(request):
    return render(request, 'add_product.html')