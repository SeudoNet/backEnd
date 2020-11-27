from django.shortcuts import render,get_object_or_404 # render_to_response
from django.http import HttpResponse, Http404
from .models import Job

# Create your views here.
##### version 1:
# def job_detail(request,job_id):
#     try:
#         job=Job.objects.get(id=job_id)
#         context={}
#         context['job_obj']=job
#         return render(request,'job_detail.html',context)  # context need to be a dict
#         #return render_to_response('job_detail.html',context)
#     except Job.DoesNotExist:
#         raise Http404('Does Not Exist')

# version 2: 
def job_detail(request,job_id): # specific job->use id
    job=get_object_or_404(Job, pk=job_id) # model(class), requirement: pk=primary key=id
    context={}
    context['job_obj']=job
    return render(request,'job_detail.html',context)  # context need to be a dict

def job_list(request):
    # jobs=Job.objects.all()
    jobs=Job.objects.filter(is_deleted=False)  # just show not deleted records
    context={}
    context['jobs']=jobs
    context['jobs_count']=Job.objects.all().count()
    return render(request,'job_list.html',context) # context need to be a dict