from django.urls import path
from .views import (index, 
    display_file,
    download_pdf,
    # your_django_endpoint,
    view_messages,
    display_pdf,
    view_certificate,
    get_pdf_url)

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', index),
    
    path('display-file/<str:file_name>/', display_file, name='display_file'),
    path('main/media/uploads/<str:filename>/', download_pdf, name='download_pdf'),
    # path('your-django-endpoint/', your_django_endpoint, name='your_django_endpoint'),
    path('view-messages/', view_messages, name='view_messages'),
    path('main/media/uploads/<str:pdf_filename>/', display_pdf, name='display_pdf'),
    path('media/certificates/<str:certificate_filename>/', view_certificate, name='view_certificate'),
    path('<str:pdf_filename>/', get_pdf_url, name='get_pdf_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
