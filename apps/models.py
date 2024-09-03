from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def  __str__(self) -> str:
        return self.name
    
class Sub_category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,related_name='sub_categories', on_delete=models.CASCADE)
    
    def  __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    sub_category = models.ForeignKey(Sub_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name 
    
class UserCeateForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email',error_messages={'exists':'This is already Exists !'})
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
    def __init__(self, *args, **kwargs):
        super(UserCeateForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        
    def save(self,commit=True):
        User = super(UserCeateForm, self).save(commit=False)
        User.email = self.cleaned_data['email']
        if commit:
            User.save()
        return User
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_message['exists'])
        return self.cleaned_data['email']
    
class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TimeField()
    
    def __str__(self):
        return self.email
    
class Order(models.Model):
    image = models.ImageField(upload_to='ecommerce/order/image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=5)
    price = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    date = models.DateField()
    
    
    def __str__(self) -> str:
        return self.name