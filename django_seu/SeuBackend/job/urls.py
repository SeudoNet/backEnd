from django.urls import path,include
# from job.views import job_detail,job_list   -->  don't need this 
from . import views

# start with job
urlpatterns = [
    # localhost: 8000/job/
    path('',views.job_list,name='job_list'),
    # http://localhost:8000/job/1
    path('<int:job_id>',views.job_detail,name='job_detail'),  # specific article, https://docs.djangoproject.com/en/3.1/ref/urls/
    path('type/<int:job_type_pk>',views.jobs_with_type, name='jobs_with_type'), # <int:job_type_pk> should be same with def jobs_with_type(inputs)
]
