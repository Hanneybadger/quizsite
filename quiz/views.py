from django.shortcuts import render

# Create your views here.
def startpage(request):
	return render(request, "quiz/quizmestart.html")

def quiz(request):
	return render(request, "quiz/quizmedog.html")

def question(request):
	return render(request, "quiz/quizmedogquestions.html")

def completed(request):
	return render(request, "quiz/quizmedogresults.html")