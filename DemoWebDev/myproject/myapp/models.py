from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Item(models.Model):
    todolist = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
