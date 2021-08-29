from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import RootDocument
from django.conf import settings
import datetime


class S3UploadCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('upload')
        if file_obj is not None:
            file_name = file_obj.name
            JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
            print(JST)
            dt_now = datetime.datetime.now(JST).strftime('%Y%m%d%H%M%S')
            if '.' in file_name:
                file_name = dt_now + '_' + '.'.join(file_name.split('.')[:-1]) + '.' + file_name.split('.')[-1]
            else:
                file_name += '_' + dt_now

            file_obj.name = file_name
            request.FILES['upload'] = file_obj

            s3_path = 's3://' + settings.AWS_STORAGE_BUCKET_NAME + '/' + settings.AWS_SCHEMA_LOCATION + '/' + file_name
            messages.success(request, s3_path)

        return super().post(request, *args, **kwargs)


class RootDocumentCreateView(S3UploadCreateView):
    model = RootDocument
    fields = ['upload',]
    success_url = reverse_lazy('uploader') # urls.py の name を指定する
    template_name = "web/uploader.html" 

