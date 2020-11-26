from django.contrib import admin
from .models import Job, JobType

# Register your models here.
@admin.register(Job)  # admin.site.register(Job,JobAdmin) # register class and model
class JobAdmin(admin.ModelAdmin):
    list_display=('title','job_type','author', 'create_time','last_updated_time',)  # tuple 
    # ordering=('-id',) # tuple , rank by id

@admin.register(JobType)    # register class and model
class JobTypeAdmin(admin.ModelAdmin):
    list_display=('id','type_name',)