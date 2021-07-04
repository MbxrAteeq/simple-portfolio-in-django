from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def index(request):    
   # Instead of this retur httpresponse line, we will use proper way to di it. and way is templates.
   # return HttpResponse("this is home section")

   #now this is how we will return templates from here and will make html file in template folder.
   return render(request, 'index.html')


#Function of about
def about(request):
    #return HttpResponse("This is my about section")
    return render(request, 'about.html')


#Function of about
def projects(request):    
    #return HttpResponse("This is my projects section")
    return render(request, 'projects.html')


#Function of contact
def contact(request):
    #return HttpResponse("This is my contact section")
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc= desc)
        ins.save()
        print("The data has been written to db")




    return render(request, 'contact.html')
