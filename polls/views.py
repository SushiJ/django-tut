from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
# fro django.template import loader

from .models import Question, Choice


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
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question})


def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/results.html", {"question": question})


def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(req, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
