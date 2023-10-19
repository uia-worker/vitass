from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadedFile
from .forms import UploadFileForm
from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# from app.forms import SimpleForm, PostForm
# from app.models import Post

from app.forms import SimpleForm
from app.forms import SimpleTestForm
import pdfplumber
from django.core.files import File

def home_redirect_view(request):
    return redirect("simple_form")

def say_hello2(request):
    return HttpResponse('Hello World')

def say_hello(request):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/hello.html" % theme, {"name": "mads"})

#def pass_request(request):
#    print("the request method is:", request.method)
#    print("the POST data is:", request.POST)
#
#    form = SimpleForm()

#def pass_request(request):
    #theme = getattr(settings, "VITASS_THEME", "bootstrap")
    #form = SimpleForm(request.POST)
    #return render(request, '/test.html', {'form':form})
    #return HttpResponse(request, "Melding")

def simple_form_view(request):
    form = SimpleForm()
    context = {"form": form, "title": "Simple Form"}
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/form.html" % theme, context)

def simple_test_view(request):
    form = SimpleTestForm() # definert i forms.py
    context = {"form": form, "title": "Simple Test"}
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/test.html" % theme, context)

def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    files = UploadedFile.objects.all()
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/upload_file.html" % theme, {'form': form, 'files': files})


def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response


def read_file(request):
    file_path = settings.BASE_DIR / "media/uploads/uml-2.5.1-formal-17-12-05.pdf"
    #file_path = settings.BASE_DIR / "media/uploads/simple.pdf"

    with pdfplumber.open(file_path) as pdf:
        first_page = pdf.pages[0]
        context = {'first_page': first_page.extract_text_simple()}
        print(context)
    
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/pdf2txt.html" % theme, context)