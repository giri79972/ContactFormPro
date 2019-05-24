from django.shortcuts import render
from .forms import ContactForm
from django.http.response import HttpResponse
from .models import ContactData
# Create your views here.

def ContactView(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            first_name=request.POST.get('first_name','')
            last_name=request.POST.get('last_name','')
            email=request.POST.get('email','')
            loc=request.POST.get('loc','')
            number=request.POST.get('number','')
            sal=request.POST.get('sal','')
            data=ContactData(first_name=first_name,
                         last_name=last_name,
                         email=email,
                         loc=loc,
                         number=number,
                         sal=sal)
            data.save()
        form=ContactForm()
        return render(request,'contact.html',{'abcd':form})
    else:
        form=ContactForm()
        return render(request,'contact.html',{'abcd':form})

