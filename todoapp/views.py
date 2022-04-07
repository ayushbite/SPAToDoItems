
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .models import Todo

# Create your views here.

def index(request):
    if request.method == "POST":
    
        #print(request.POST)
        added_date = timezone.now()
        item = request.POST["items"]
        #print(added_date)
        #print(item)
        Todo.objects.create(created_at=added_date,item=item)


    todo_items=Todo.objects.all().order_by("-created_at") 
    context={
       'lists':todo_items
    }   
        

    return render(request,'index.html',context=context)


def delete_todo(request,cus_todo_id):
    #print(cus_todo_id)   
    Todo.objects.get(id=cus_todo_id).delete()
    return HttpResponseRedirect("/")



    
