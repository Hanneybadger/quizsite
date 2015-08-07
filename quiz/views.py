# coding: utf-8
from quiz.models import Quiz

from django.shortcuts import render

from django.shortcuts import redirect



# quizzes = {
# 	"klassiker": {
#    		"name": u"Klassiska böcker",
# 	   	"description": u"Hur bra kan du dina klassiker?"
# 	},
# 	"fotboll": {
# 	   	"name": u"Största fotbollslagen",
# 	   	"description": u"Kan du dina lag?"
# 	},
# 	"kanda-hackare": {
# 	    	"name": u"Världens mest kända hackare",
# 	    	"description": u"Hackerhistoria är viktigt, kan du den?"	},
# }


# Create your views here.
def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/quizmestart.html", context)

def quiz(request, slug):
	context = {
		"quiz": Quiz.objects.get(slug=slug),
#		"quiz_slug": slug,
	}
	return render(request, "quiz/quizmedog.html", context)

def question(request, slug, number):
	number = int(number)
	quiz = Quiz.objects.get(slug=slug)
	questions = quiz.questions.all()
	if number > questions.count():
		return redirect("completed_page", quiz.slug)
	question = question = questions[number - 1]
	
	context = {
		"question_number": number,
		"question": question.question,
		"answer1": question.answer1,
		"answer2": question.answer2,
		"answer3": question.answer3,
		"answer4": question.answer4,
		"quiz": quiz,
	}

	return render(request, "quiz/quizmedogquestions.html", context)

def completed(request, slug):
	context = {
		"correct": 12,
		"total": 20,
		"quiz_slug": slug,
	}

	return render(request, "quiz/quizmedogresults.html", context)

