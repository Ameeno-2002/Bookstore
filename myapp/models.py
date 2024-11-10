from django.db import models
from PIL import Image
from django.conf import settings

class Textmainpg(models.Model):
    title_name=models.CharField(max_length=100,default="Defult Title")
    body_title=models.TextField()
    def __str__(self):
        return self.title_name


class Address(models.Model):
    street_ad=models.CharField(max_length=50)
    state_ad=models.CharField(max_length=20)
    coutry_name=models.CharField(max_length=37)
    def __str__(self):
        return self.street_ad
    
class BookProduct(models.Model):
    
    x=[
        ('action', 'Action'),
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
        ('poetry', 'Poetry'),
        ('business', 'Business'),
        ('health_wellness', 'Health & Wellness'),
        ('travel', 'Travel'),
        ('cooking', 'Cooking'),
        ('education', 'Education'),
    ]
    
    prod_img=models.ImageField(upload_to='photos/%y/%m/%d', null=True, blank=True)
    prod_name=models.CharField(max_length=35,verbose_name='book_name')
    book_detail=models.CharField(max_length=25,verbose_name='detail')
    book_catagory=models.CharField(max_length=50,null=True,choices=x)
    price =models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    author=models.CharField(max_length=14 ,default="Author name")
    active= models.BooleanField(default=True)
    

    
    def __str__(self):
        return f"{self.prod_name} "
        

#For The book List
class BooksList(models.Model):
    book_img=models.ImageField(upload_to='photos/%y/%m/%d', null=True, default='../static/images/nobookimage.png')
    book_name=models.CharField(max_length=12,default='Book_name')
    book_disc=models.CharField(max_length=25,default='detail')
    book_price=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    active= models.BooleanField(default=True)
    def __str__(self):
        return f"{self.book_name} "