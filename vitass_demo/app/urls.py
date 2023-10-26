"""
from django.urls import path

from app.views import (
    home_redirect_view,
    simple_form_view,
    post_form_view,
    test_markdownify,
)

urlpatterns = [
    path("", home_redirect_view, name="home_redirect"),
    path("simple-form/", simple_form_view, name="simple_form"),
    path("post-form/", post_form_view, name="post_form"),
    path("test-markdownify/", test_markdownify, name="test_markdownify"),
]
"""
from django.urls import path
from . import views

from app.views import (
    home_redirect_view,
    simple_form_view,
    upload_file_view,
    simple_test_view,
    say_hello,
    say_hello2,
)

urlpatterns = [
    path("", home_redirect_view, name="home_redirect"),
    path("simple-form/", simple_form_view, name="simple_form"),
    path("upload/", upload_file_view, name='upload_file'),
    path("download/<int:file_id>/", views.download_file, name='download_file'),
    path("pdf2txt/", views.read_file, name='read_file'),
    path("test/", views.simple_test_view, name="simple_test"),
    path("say_hello/", views.say_hello, name='say_hello'),
    path("say_hello2/", views.say_hello2, name='say_hello2'),
    path("movies/", views.movies, name="movies"),
    path("movies2/", views.movies2, name="movies2"),
    path("movies3/", views.movies3, name="movies3"),
    path("movies/<int:id>/", views.detail, name="detail"),
    path("add/", views.add, name="add"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("form/", views.register, name="register"),
    path("prompt/", views.prompt, name="prompt"),
    path("promptform/", views.promptform, name="promptform"),
    path("prompts/<int:id>/", views.promptdetail, name="promptdetail"),
    
]
