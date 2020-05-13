import io
from contextlib import redirect_stdout
from django.core.management.base import BaseCommand
from common.models import Job


class Command(BaseCommand):
    def add_arguments(self, parse):
        parse.add_argument("job_id", type=str)

    def handle(self, *args, **options):
        job_id = options['job_id']
        print(job_id)
        j = Job.objects.get(job_id=job_id)
        f = io.StringIO()
        with redirect_stdout(f):
            exec(j.code)
        j.result = f.getvalue()
        j.completed = True
        print('>>>', j.result)
        j.save()
