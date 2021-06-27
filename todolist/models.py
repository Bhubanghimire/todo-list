from django.db import models

# Create your models here.
class Todolist(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    text = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text