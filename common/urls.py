from django.urls import path, include
from common.views.main import *

urlpatterns = [
    path("job", job, name="job"),
    path("job/set", set_job, name="set_job"),
    path("job/get", get_job, name="get_job"),
]
