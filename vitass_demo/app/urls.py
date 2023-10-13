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
)

urlpatterns = [
    path("", home_redirect_view, name="home_redirect"),
    path("simple-form/", simple_form_view, name="simple_form"),
    path("upload/", upload_file_view, name='upload_file'),
    path("download/<int:file_id>/", views.download_file, name='download_file'),
    path("pdf2txt/", views.read_file, name='read_file'),
    path("test/", views.simple_test_view, name="simple_test"),
]
