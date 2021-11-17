from .models import Content

def get_contents():
    return Content.objects.values('pk', 'file_name')