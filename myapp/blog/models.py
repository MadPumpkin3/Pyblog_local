from django.db import models

# Create your models here.

class PyBlog(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=100)
    update_dt = models.DateTimeField(auto_now=True)
    regist_dt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'py_blog'