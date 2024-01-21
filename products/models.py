from django.db import models

#create models here

category_type = (
    ('Apartment', 'apartment'),
    ('House', 'house'),
    ('Studio', 'studio')
)

category_value = (
    ('For Sale', 'sale'),
    ('For Rent', 'rent')
)

class ProductsModel(models.Model):
    title= models.CharField(max_length= 255)
    description= models.TextField()
    price= models.FloatField()
    active= models.BooleanField(null= True,default=False, blank=True)
    address= models.TextField(null= True)
    room_count= models.FloatField(null=True)
    bathroom_count= models.FloatField(null=True)
    square_meters= models.FloatField(null=True)
    property_type = models.CharField(choices=category_type, max_length=9 , default='Apartment')
    property_feature = models.CharField(choices=category_value, max_length=8 , default='For Sell')
    images= models.ImageField(upload_to='media/', blank= True, null= True)


    # image_name= models.ImageField(upload_to="products/")
    slug = models.SlugField(null=True, blank=True, unique=True)

def __str__(self):
    return self.title


