from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
import datetime
from django.views.decorators.http import require_http_methods
from .forms import UploadFileForm

def index(request):
	return HttpResponse('Hello there!')




def handle_uploaded_file(f):
    with open('name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponse("success")
	else:
		form = UploadFileForm()
	return render(request, 'example/upload.html', {'form':form})