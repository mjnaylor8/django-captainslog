import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download_file(request):
    file_path = settings.BASE_DIR + request.path
    # print(request.path, file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/json")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            # response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    raise Http404