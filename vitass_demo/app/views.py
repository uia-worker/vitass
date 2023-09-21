from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#from app.forms import SimpleForm, PostForm
#from app.models import Post

from app.forms import SimpleForm

def home_redirect_view(request):
    return redirect("simple_form")

def simple_form_view(request):
    form = SimpleForm()
    context = {"form": form, "title": "Simple Form"}
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/form.html" % theme, context)
