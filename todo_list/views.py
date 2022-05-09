from django.shortcuts import render
from .models import List
from .forms import ListForm

# Create your views here.
def home(request):
    if request.method == "POST":  # add form input item to database
        if request.POST["item"] != "" :
            form = ListForm(request.POST)
            form.save()
    
    all_items = List.objects.all
    return render(request,'home.html',{'all_items': all_items})


def about(request):
    return render(request,'about.html',{})