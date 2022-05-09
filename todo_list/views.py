from django.shortcuts import render, redirect
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


def delete(request, item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    request.session['undo_item'] = item.item
    messages.warning(request,('Item "{}" Has Been Deleted!'.format(item.item)))
    return redirect('home')

def undo(request):
    undo_item = request.session.get('undo_item')
    item = List(item=undo_item)
    item.save()
    messages.success(request,('Undo: Item "{}" Has Been Retrieved!'.format(undo_item)))
    return redirect('home')

def crossoff(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return redirect('home')