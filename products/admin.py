from pyexpat import model
from django.contrib import admin

from .models import ProductsModel
# Register your models here.


#admin.site.register(Product)




class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = ProductsModel

admin.site.register(ProductsModel, ProductAdmin)
