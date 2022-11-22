from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create edit time
from django.utils import timezone
# Import Todo model for use in add_todo function view
from app.models import Todo
# Import HttpResponseRedirect for use in add_todo function to redireect to homepage
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
  template = 'app/index.html'
  # Create todo list item
  todo_items = Todo.objects.all().order_by('-added_date')
  return render(request, template, {'todo_items': todo_items})

# Function that adds task
@csrf_exempt
def add_todo(request):
  current_date = timezone.now()
  # Get value of input
  content = request.POST['content']
  # Create Todo list objects
  list_obj = Todo.objects.create(added_date=current_date, text=content)
  # Amount of tasks
  length_of_tasks = Todo.objects.all().count()
  # Renders view on homepage
  return HttpResponseRedirect('/')


# Delete function that takes in request and id parameter from url
@csrf_exempt
def delete_todo(request, todo_id):
  # Delete task by id
  Todo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect('/')