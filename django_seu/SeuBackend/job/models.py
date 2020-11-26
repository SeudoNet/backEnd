from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class JobType(models.Model):
    type_name = models.CharField(max_length=50,default='') 
    
    def __str__(self):
        return self.type_name

class Job(models.Model):
    title= models.CharField(max_length=100,default='')
    job_type=models.ForeignKey(JobType, on_delete=models.DO_NOTHING, default='',null=True,blank=True) # ForeignKey to link job_type to JobType
    content=models.TextField(default='')
    author=models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1) # add foreign key to relate auther to user
                                                                            # on_delete: delete job won't delete user
                                                                            # default auther name:1 
    create_time=models.DateTimeField(default=timezone.now)
    # create_time=models.DateTimeField(auto_now_add=True) # same as above
    last_updated_time=models.DateTimeField(auto_now=True) # auto use the time right now
    is_deleted=models.BooleanField(default=False) 
    readed_num=models.IntegerField(default=0)

    def __str__(self):   # show title name on admin
        return '<Job: %s>' % self.title

