from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # Add Todo url/path
  path('add_todo/', views.add_todo),
  # Delete Todo url/path
  path('delete_todo/<int:todo_id>/', views.delete_todo)
]