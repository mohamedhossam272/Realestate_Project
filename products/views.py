from urllib import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView, View

from .models import ProductsModel
import urllib.request

from django.http import Http404

from django.db.models import Q

from .forms import ContactSummaryForm






def home_page(request):
    object_list= ProductsModel.objects.all()

    context= {
        'object_list':object_list
    }
    return render(request, 'home2.html', context)

class HomePage(ListView):
    queryset= ProductsModel.objects.all()
    template_name= 'home2.html'

    def get_context_data(self, *args, **kwargs):
        context= super(HomePage, self).get_context_data(*args, **kwargs)
        print(context)
        return context

from django.http import Http404

def product_detail_view(requset, pk=None):
    # instance = Product.objects.get(pk=pk) #id
    # instance = get_object_or_404(Product, pk=pk)
    try: 
        instance = ProductsModel.objects.get(id=pk)

    except ProductsModel.DoesNotExist:
        print('no product here')
        raise Http404("product doesn't exist")

    context = {
        "object": instance
    }
    return render(requset, "product/detail.html", context)

def product_detail_view(requset, pk=None):
    # instance = ProductsModel.objects.get(pk=pk) #id
    instance = get_object_or_404(ProductsModel, pk=pk)
    context = {
        "object": instance
    }
    return render(requset, "home3.html", context)

class ProductDetailView(DetailView):
    queryset= ProductsModel.objects.all()
    template_name= 'home3.html'

    def get_queryset(self, *args, **kwargs):
        request= self.request
        return ProductsModel.objects.filter(active__icontains = True)
    

class HomeView(ListView):
    queryset= ProductsModel.objects.all()
    template_name= 'index.html'

    def get_queryset(self, *args, **kwargs):
        request= self.request
        query= (request.GET.get('q'))
        if query is not None:
            lookups=(
                Q(title__icontains=query) |
                Q(price__icontains=query) |
                Q(property_feature= query) |
                Q(property_type= query)

            )
            return ProductsModel.objects.filter(lookups).distinct()
        return ProductsModel.objects.all()
    


class ProductView(DetailView):
    model= ProductsModel.objects.all()
    template_name= 'property-list.html'

class ContactSummaryView(View):
    
    def get(self, *args, **kwargs):
        form= ContactSummaryForm()
        context={
            'form':form

        }

        return render(self.request, 'contact.html', context)





