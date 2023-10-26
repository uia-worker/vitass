from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Prompt, UploadedFile
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
from .models import Movie
from. models import User
from. models import Prompt


data2 = {"movies" : Movie.objects.all()}

data = {
    "movies": [
        {
            "id":5,
            "title":"Jaws",
            "year":1986,
        },
        {
            "id":6,
            "title":"Sharkando",
            "year":1990,

        },
        {
            "id":7,
            "title":"The Meg",
            "year":2000,

        }



    ]
}

def home_redirect_view(request):
    return redirect("simple_form")

def movies(request):
    #theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, 'bootstrap/movies.html', data)

def movies2(request):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    data = Movie.objects.all()
    return render(request, "%s/movies2.html" % theme, {'movies':data})

def movies3(request):
    data = Movie.objects.all()
    return render(request, "bootstrap/movies3.html", {'movies': data})

def say_hello2(request):
    return HttpResponse('Hello World')

def say_hello(request):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/hello.html" % theme, {"name": "mads"})

def detail(request, id):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    data = Movie.objects.get(pk=id)
    return render(request, "%s/detail.html" % theme, {"movie": data})

def promptdetail(request, id):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    data = Prompt.objects.get(pk=id)
    return render(request, "%s/promptdetail.html" % theme, {"prompt": data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies2')
    return render(request, 'bootstrap/add.html')

def prompt(request):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    data = Prompt.objects.all()
    return render(request, "%s/prompt.html" % theme, {'prompts':data})

def promptform(request):
    navn = request.POST.get('navn')
    tittel = request.POST.get('tittel')
    tekst = request.POST.get('tekst')

    if tittel and tekst and navn:
        prompt = Prompt(tittel=tittel, tekst=tekst, navn=navn)
        prompt.save()
        return HttpResponseRedirect('/prompt')
    return render(request, 'bootstrap/promptform.html')

def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    telephone = request.POST.get('telephone')
    name = request.POST.get('name')


    if username and password and email and name and telephone:
        user = User(username=username, password=password, email=email, name=name)
        user.save()
        return HttpResponseRedirect('/movies2')
    return render(request, 'bootstrap/form.html')

def delete(request, id):
    Movie.objects.get(pk=id).delete()
    return HttpResponseRedirect('/movies2')

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