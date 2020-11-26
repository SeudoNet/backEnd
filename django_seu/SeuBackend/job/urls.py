from django.urls import path,include
# from job.views import job_detail,job_list   -->  don't need this 
from . import views

urlpatterns = [
    # localhost: 8000/job/id
    # path('job/<int:job_id>',views.job_detail,name='job_detail'),
    path('<int:job_id>',views.job_detail,name='job_detail'),
    # localhost: 8000/job/
    path('',views.job_list,name='job_list'),
]
