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
	questions = quiz.questions.all().order_by("id")

	if request.POST:
		answer = int(request.POST["answer"])

		saved_answers = {}
		if quiz.slug in request.session:
			saved_answers = request.session[quiz.slug]

		saved_answers[str(number)] = answer
		request.session[quiz.slug] = saved_answers

		if questions.count() == number:
			return redirect("completed_page", quiz.slug)

		else:
			return redirect("question_page", quiz.slug, number +1)

	question = questions[number - 1]
	
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
	quiz = Quiz.objects.get(slug=slug)
	questions = quiz.questions.all().order_by("id")
	saved_answers = request.session[slug]
	num_correct_answers = 0
	for counter, question in enumerate(questions):
		if question.correct == saved_answers[str(counter + 1)]:
			num_correct_answers += 1

	context = {
		"correct": num_correct_answers,
		"total": questions.count(),
		"quiz": quiz,
		"questions": questions,
		"saved_answers": saved_answers,
	}

	return render(request, "quiz/quizmedogresults.html", context)

