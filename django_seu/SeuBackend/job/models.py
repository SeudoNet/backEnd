from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    title= models.CharField(max_length=40)
    content=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)
    # create_time=models.DateTimeField(auto_now_add=True)
    last_updated_time=models.DateTimeField(auto_now=True) # auto use the time right now
    author=models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1) # add foreign key to relate auther to user
                                                                            # on_delete: delete job won't delete user
                                                                            # default auther name:1 
    is_deleted=models.BooleanField(default=False) 
    readed_num=models.IntegerField(default=0)
    def __str__(self):   # show title name on admin
        return '<Job: %s>' % self.title


