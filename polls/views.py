from django.shortcuts import render, HttpResponse, get_list_or_404
# from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }

    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(req, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_list_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question})


def results(req, question_id):
    response = "You're looking at result of question %s."
    return HttpResponse(response % question_id)


def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
