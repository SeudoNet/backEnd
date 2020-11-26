from django.contrib import admin
from .models import Job

# Register your models here.
@admin.register(Job)  # admin.site.register(Job,JobAdmin) # register class and model
class JobAdmin(admin.ModelAdmin):
    list_display=('id','title','content', 'author', 'is_deleted','create_time','last_updated_time',)  # tuple 
    ordering=('-id',) # tuple , rank by id



