#from django.shortcuts import render

from django.http import HttpResponse, Http404
from . import models
from django.shortcuts import render

# Create your views here.
def index(req):
    # return HttpResponse("From Polls App")
    #return HttpResponse("Hello, world. a35e2f4a is the polls index.")
    latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(req, 'polls/index.html', context)

def owner(req):
    return HttpResponse("Hello, world. a35e2f4a is the polls index.")

def results(req, question_id):
    response = "You're looking at the results of question %s."
    try:
        that_question = models.Question.objects.get(pk=question_id)
    except models.Question.DoesNotExist:
        raise Http404("Question with %s id was not found" % question_id)
    ctx = {
            "that_question": that_question,
            "question_id": question_id
            }
    return render(req, "polls/results.html", ctx)

def vote(req, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)
