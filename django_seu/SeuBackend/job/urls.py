from django.urls import path,include
# from job.views import job_detail,job_list   -->  don't need this 
from . import views

# start with job
urlpatterns = [
    # localhost: 8000/job/
    path('',views.job_list,name='job_list'),
# http://localhost:8000/job/1
    path('<int:job_id>',views.job_detail,name='job_detail'),  # specific article, https://docs.djangoproject.com/en/3.1/ref/urls/
    
]
