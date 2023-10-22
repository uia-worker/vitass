# https://studygyaan.com/django/how-to-upload-and-download-files-in-django
from django.db import models

class UploadedFile(models.Model):
	file = models.FileField(upload_to='uploads/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

class Movie(models.Model):
	title = models.CharField(max_length=200)
	year = models.IntegerField()

	def __str__(self):
		return f'{self.title} from {self.year}'
	
class User(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	telehpone = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.username} {self.name} {self.password} {self.email} {self.telehpone}'

