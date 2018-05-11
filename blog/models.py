from django.db import models

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.CharField(max_length = 500)
    sys_cret_dt = models.DateField(auto_now_add=True)
    sys_chgt_dt = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

