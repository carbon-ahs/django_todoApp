from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Item has been added successfully!!')
            context = {
                'keys' : 'values',
                'method' : request.method,
                'all_items' : all_items,
            }
            return render(request, 'home.html', context)

    else:
        all_items = List.objects.all
        context = {
            'keys' : 'values',
            'all_items' : all_items,
            'method' : request.method,
        }
        return render(request, 'home.html', context)

def about(request):
    co_name = "TandovIT LTD."

    context = {
        'co_name': co_name,
        'keys' : 'values', 
        
    }
    return render(request, 'about.html', context)

def cut_off(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncut(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = False
    item.save()
    return redirect('home')

def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, 'Item has been deleted :( ')
            
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk = list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            
            messages.success(request, 'Item has been Edited successfully!!')
            context = {
                'keys' : 'values',
                'method' : request.method,
            }
            #return render(request, 'edit.html', context)
            return redirect('home')
    else:
        item = List.objects.get(pk = list_id)
        context = {
            'keys' : 'values',
            'item' : item,
            'method' : request.method,
        }
        return render(request, 'edit.html', context)
