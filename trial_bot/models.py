from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect,reverse

# Create your models here.


class Chats(models.Model):
	que=models.CharField(max_length=500)
	pro_ans=models.CharField(max_length=500)
	sug_ans=models.CharField(max_length=500)
	name=models.CharField(max_length=50)


	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# 	return reverse('groups:join',kwargs={'pk':self.pk})

