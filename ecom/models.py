from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    sname = models.CharField(max_length=30)
    semail = models.CharField(max_length=50)
    ssub = models.CharField(max_length=50)
    smessage = models.TextField()

    def __str__(self):
        return self.sname
    
class catagory(models.Model):
    cid = models.AutoField(primary_key=True)
    cname =models.CharField(max_length=50)
    
    def __str__(self):
        return self.cname
    
class product(models.Model):
    pid= models.AutoField(primary_key=True)
    pname=models.CharField(max_length=30)
    pprice = models.IntegerField()
    pdiscount = models.IntegerField()
    pimg = models.ImageField(upload_to='pimg/')
    pdisc= models.TextField()
    c_id= models.ForeignKey('catagory',on_delete=models.CASCADE)

    def __str__(self):
        return self.pname
    

class Cart(models.Model):
    cartid= models.AutoField(primary_key=True)
    p_id= models.ForeignKey('product',on_delete=models.CASCADE)
    u_id= models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.p_id.pprice * self.quantity
    

class order(models.Model):
    STATUS_CHOICE =(
        ("pendding" , "pendding"),
        ("confirm" , "confirm"),
        ("cansal" , "cansal"),
        ("delevered" , "delevered"),

    )

    oid =models.AutoField(primary_key=True)
    u_id = models.ForeignKey(User,on_delete=models.CASCADE)
    uname = models.CharField(max_length=70)
    email = models.CharField(max_length=50) 
    phone = models.BigIntegerField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)   
    zip = models.IntegerField()
    odate = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=9, choices= STATUS_CHOICE,default="pendding")


class o_item(models.Model):
    otid = models.AutoField(primary_key=True)
    o_id = models.ForeignKey(order,on_delete=models.CASCADE)
    p_id = models.ForeignKey('product',on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.BigIntegerField()

    
    


    
    


