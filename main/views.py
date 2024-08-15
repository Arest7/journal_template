from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse, Http404
from django.conf import settings
import os
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
# from .models import ContactMessage
from django.http import JsonResponse

from django.http import FileResponse
from urllib.parse import quote

# Create your views here.
def index(request):
    news =  Articles.objects.order_by('datenow')
    documents = Articles.objects.all()
    return render(request, 'main/theme-clean1.html', {'news': news})




def view_certificate(request, certificate_filename):
    file_path = 'news/media/certificates/' + certificate_filename
    with open(file_path, 'rb') as file:
        response = FileResponse(file)
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = f'inline; filename="{quote(certificate_filename)}"'
    return response



def download_pdf(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

            # Set the Content-Length header to the size of the file
            response['Content-Length'] = os.path.getsize(file_path)

            return response
    else:
        raise Http404("File not found")


# @csrf_exempt
# def your_django_endpoint(request):
#     if request.method == 'POST':
#         try:
#             # Get data from the POST request
#             data = json.loads(request.body.decode('utf-8'))

#             # Save the data to the ContactMessage model
#             contact_message = ContactMessage.objects.create(
#                 name=data.get('name'),
#                 email=data.get('email'),
#                 subject=data.get('subject'),
#                 message=data.get('message'),
#             )

#             # Respond with a JSON success message
#             return JsonResponse({'status': 'success'})
#         except Exception as e:
#             # Handle exceptions, log errors, etc.
#             return JsonResponse({'status': 'error', 'message': str(e)})

#     # If the request method is not POST, respond with an error
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'})




def view_messages(request):
    messages = ContactMessage.objects.all()
    return render(request, 'view_messages.html', {'messages': messages})




def display_file(request, file_name):

    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    return response

from urllib.parse import unquote

def display_pdf(request, pdf_filename):
    try:
        # Decode the URL-encoded filename
        pdf_filename = unquote(pdf_filename)

        pdf_file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', pdf_filename)

        # Check if the file exists
        if os.path.exists(pdf_file_path):
            with open(pdf_file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')

            response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
            return response
        else:
            return HttpResponse("File not found", status=404)
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error in display_pdf: {str(e)}")
        return HttpResponse("Internal Server Error", status=500)

def get_pdf_url(request, pdf_filename):
    pdf_url = reverse('main:display_pdf', kwargs={'pdf_filename': pdf_filename})
    return JsonResponse({'pdf_url': pdf_url})
