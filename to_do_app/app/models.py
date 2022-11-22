from django.db import models

# Create your models here.

class Todo(models.Model):
  class Meta:
    verbose_name_plural = 'Todos'
    
  added_date = models.DateTimeField()
  text = models.CharField(max_length=200)

  # Convert text to readable string
  def __str__(self) -> str:
    return self.text


