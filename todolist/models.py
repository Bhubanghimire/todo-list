from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todolist(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    text = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text