import os
import uuid
import sh
from django.conf import settings


def set_k8s_job(job):
    job_name = uuid.uuid4().hex
    y = """apiVersion: batch/v1
kind: Job
metadata:
  name: %s
spec:
  template:
    spec:
      containers:
      - name: pygoonk
        image: druuu/pygoonk:0.5
        command: ['/usr/bin/python3', 'manage.py', 'run', '%s']
      restartPolicy: Never""" % (job_name, job.job_id)
    jf = "/tmp/" + job_name
    with open(jf, 'w') as f:
        f.write(y)
    sh.kubectl("create", "-f", jf, "-n", settings.K8S_NAMESPACE)
    os.remove(jf)
