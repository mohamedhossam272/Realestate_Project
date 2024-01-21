from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from .forms import LogInForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth import get_user_model
from django.contrib.auth import logout



def index_page(request):
    return render(request, "index.html",{})


def about_page(request):
    return render(request, "about.html", {})


def contact_page(request):
    return render(request, "contact.html", {})

def property_agent(request):
    return render(request, "property-agent.html", {})

def property_list(request):
    return render(request, "property-list.html", {})

def property_type(request):
    return render(request, "property-type.html", {})



# def home_page(request):
#     context = {
#         "title":"Hello World!",
#         "contact":"welcome to the home page"
#     }
#     return render(request, "home3.html", context)


# def about_page(request):
#     context = {
#         "title":"about page",
#         "contact":"welcome to the about page",


#         "name":"2846127845128976478126"
#     }
#     return render(request, "home3.html", context)


# def contact_page(request):
#     context = {
#         "title":"contact page",
#         "contact":"welcome to the contact page"
       
#     }
#     return render(request, "home3.html", context)




# def contact_page(request):
#     context = {
#         "title":"contact page",
#         "contact":"welcome to the contact page"
       
#     }
#     return render(request, "contact/view.html", context)

# def contact_page(request):
#     context = {
#         "title":"contact page",
#         "contact":"welcome to the contact page"
       
#     }
#     if request.method == "POST":
#         print(request.POST)
#         print(request.POST.get("fullname"))
#     return render(request, "contact/view2.html", context)



# def contact_page(request):
#     context = {
#         "title":"contact page",
#         "contact":"welcome to the contact page"
       
#     }
#     if request.method == "POST":
#         print(request.POST)
#         print(request.POST.get("fullname"))
#         print(request.POST.get("email"))
#         print(request.POST.get("content"))
#     return render(request, "contact/view2.html", context)




# def contact_page(request):
#     contact_form = ContactForm()
#     context = {
#         "title":"contact page",
#         "contact":"welcome to the contact page",
#         "form":contact_form,
#     }
#     if request.method == "POST":
#         print(request.POST)
#         print(request.POST.get("fullname"))
#         print(request.POST.get("email"))
#         print(request.POST.get("content"))
#     return render(request, "contact/view3.html", context)


# def contact_page(request):
#     contact_form = ContactForm(request.POST or None)
#     context = {
#         "title":"contact page",
#         "contact":"welcome to the contact page",
#         "form":contact_form,
#     }
#     if  contact_form.is_valid():
#         print(contact_form.cleaned_data)
#     return render(request, "contact/view3.html", context)




def register_page(request):
    form = LogInForm(request.POST or None)
    if  form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})

def login_page(request):
    form = LogInForm(request.POST or None)
    print(request.user.is_authenticated)
    if  form.is_valid():
        print(form.cleaned_data)

    context = {
        "form":form
    }
    return render(request, "auth/login.html", context)

def login_page(request):
    form = LogInForm(request.POST or None)
    print(request.user.is_authenticated)
    context = {
        "form":form
    }
    if  form.is_valid():
        print(form.cleaned_data)
        context['form'] = LogInForm()


    return render(request, "auth/login.html", context)




def login_page(request):

    form = LogInForm(request.POST or None)

    print(request.user.is_authenticated)
    
    context = {
        "form":form
    }
    if  form.is_valid():
        print(form.cleaned_data)


        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username= username, password= password)
        print('user is :',user)

        if user is not None:
            login (request, user)
            #context['form'] = LogInForm()
            return redirect("/")
        else:
            print("Error")
        print(request.user.is_authenticated)

    return render(request, "auth/login.html", context)



# def home_page(request):
#     context = {
#         "title":"Hello World!",
#         "contact":"welcome to the home page",
        
#     }
#     if request.user.is_authenticated:
#         context["premium_content"]= "Yeahhhh"
#     if request.user.is_authenticated:
#         context["premium_content_2"]= "heloo"
#     return render(request, "home4.html", context)




def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if  form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})




User = get_user_model() 

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    
    if  form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        new_user = User.objects.create_user(username, email, password)

        print(new_user)
        return redirect("/")
    return render(request, "auth/register.html", context)




def logout_view(request):
    logout(request)        
    return redirect("/")
