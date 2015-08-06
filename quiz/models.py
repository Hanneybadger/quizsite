from django.db import models

# Create your models here.
class Quiz(models.Model):
	name = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150)
	description = models.TextField()

class Question(models.Model):
	quiz = models.ForeignKey(Quiz)
	question = models.TextField()
	answer1 = models.CharField(max_length=250)
	answer2 = models.CharField(max_length=250)
	answer3 = models.CharField(max_length=250)
	answer4 = models.CharField(max_length=250)
	correct = models.PositiveIntegerField()

	