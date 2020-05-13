import uuid
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from common.models import Job
from common.utils import set_k8s_job


def job(request):
    job_id = uuid.uuid4().hex
    return render(request, "job.html", {'job_id': job_id})


def set_job(request):
    job_id = request.POST['jobid']
    code = request.POST['code']
    try:
        j = Job.objects.get(job_id=job_id)
        j.code = code
        j.completed = False
        j.save()
    except Job.DoesNotExist:
        j = Job.objects.create(job_id=job_id, completed=False, code=code)
    set_k8s_job(j)
    url = "%s?jobid=%s" % (reverse('get_job'), job_id)
    return HttpResponseRedirect(url)


def get_job(request):
    job_id = request.GET['jobid']
    j = Job.objects.get(job_id=job_id)
    return render(request, "get_job.html", {'job': j})
