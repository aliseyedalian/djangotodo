from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":  # add form input item to database
        if request.POST["item"] != "" :
            form = ListForm(request.POST)
            form.save()
            messages.success(request,('Item "{}" Has Been Added To List!'.format(request.POST["item"])))
    
    all_items = List.objects.all
    return render(request,'home.html',{'all_items': all_items})


def about(request):
    return render(request,'about.html',{})