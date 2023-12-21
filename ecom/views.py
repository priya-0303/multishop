from django.shortcuts import render,redirect
from django.contrib import messages
from .models import product,Contact,Cart,o_item,order
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required


# Create your views here.

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')


def index(request):
    return render(request,'index.html')

def shop(request):
    data = product.objects.all()
    return render(request,'shop.html',{'data': data})

def detail(request):
    return render(request,'detail.html')

def checkout(request):
    return render(request,'checkout.html')

@login_required(login_url='/login/')
def carts(request):
    c_data = Cart.objects.filter(u_id=request.user)
    g_total = 0
    for ct in c_data:
        g_total += ct.sub_total()

    return render(request,'cart.html',{'c_data':c_data,'g_total':g_total})

@login_required(login_url='/login/')
def checkout(request):
    c_data = Cart.objects.filter(u_id=request.user)
    g_total = 0
    for ct in c_data:
        g_total += ct.sub_total()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        payment = request.POST['payment']

        if payment == '1':
            o = order(u_id=request.user,name=name,email=email,phone=phone,address=address,country=country,city=city,state=state,zip=zip,oamount=g_total)
            o.save()

            last_order = order.objects.last()

            for cd in c_data:
                p = product.objects.get(pid=cd.p_id.pid)
                o_item(o_id=last_order,p_id =p,quantity=cd.quantity,sub_total=cd.sub_total()).save()
                cd.delete()

                messages.success(request,'order summary generated..')
                return render('/confirmorder/'+ str(last_order))
            

    return render(request,'checkout.html',{'g_total':g_total})




@login_required(login_url='/login/')
def add_cart(request,pid):
    p = product.objects.get(pid=pid)
    if Cart.objects.filter(p_id=p,u_id=request.user).exists():
        messages.warning(request,"already in cart...")
        return redirect('/cart/')
    else:
        Cart(p_id=p,u_id=request.user,quantity=1).save()
        messages.warning(request,"Add in cart...")

    return redirect('/cart/')

@login_required(login_url='/login/')
def plus_cart(request,cid):
    c = Cart.objects.get(cartid=cid)
    c.quantity += 1
    c.save()
    return redirect('/cart/')

@login_required(login_url='/login/')
def minus_cart(request,cid):
    c = Cart.objects.get(cartid=cid)
    if c.quantity <= 1:
        c.delete()
        return redirect('/cart/')

    else:
        c.quantity -= 1
        c.save()
        return redirect('/cart/')
    
def confirmorder(request,oid):
    o_data = order.objects.get(oid=oid)
    item_data = o_item.objects.filter(o_id=oid)
    return render(request,'confirmorder.html',{'order_data':o_data,'order_item_data':item_data})


def myorders(request):
    o_data = order.objects.filter(u_id=request.user)
    return render(request,'myorders.html',{'o_data':o_data})

def search(request):
    query = request.GET.get('query','')
    data = product.objects.filter(pname__icontains=query)
    return render(request,'search.html',{'data':data,'query':query})

def delete_cart(request,cid):
    c = Cart.objects.get(cartid=cid)
    c.delete()
    return redirect('/cart/')

def cat_prod(request,id):
    cat_prod_data = product.objects.filter(c_id=id)
    return render(request,'cat_prod.html',{'cat_prod_data': cat_prod_data})

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg =request.POST['messages']
        
        s = Contact(sname=name,semail=email,ssub=subject,smessage=msg)
        s.save()
        print("data added..")
        messages.success(request,"data added..")
        return redirect('/')
    
    return render(request,'contact.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2: 
            if User.objects.filter(username=uname).exists():
                messages.success(request,'Username already exist...')
                print("Username already exist...")
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.success(request,'email already exist...')
                print("Email already exist...")
                return redirect('/register/')
            else:    
                u = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1)
                u.save()
                messages.success(request,'User created...')
                print("User created...")
                return redirect('/')
        else:
            messages.error(request,'passwords does not match...')
            print("passwords does not match...")
            return redirect('/register/')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pass']

        User = auth.authenticate(username=uname,password=password)

        if User is not None:
            auth.login(request,User)
            messages.success(request,'you successfully logged In..')
            print("logged In...")
            return redirect('/')
        else:
            messages.error(request,'invalid credentials...')
            print("invalid credentials...")
            return redirect('/login/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.error(request,'your account is LOGGED OUT..')
    print("logged out ..")
    return redirect('/')














