from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import Question, Choice

def polls_home_view(request):

    # q = Question(question_text="what is your name", pub_date=timezone.now())
    # c = Choice(choice_text="hey its me", votes=1, question=q)
    # q.save()
    # c.save()
    # q.choice_set.create(choice_text="not so much", votes=3)
    # print(q.__str__(), "kkk kj kjk")
    # print(c.__str__(), c.votes, c.question)
    # print(q.choice_set.all())

    qt = Question.objects.order_by('pub_date')
    t = [q.question_text for q in qt]

    print(qt, "printing qt")
    print(t)
    # for item in qt:
    #     print(item.id, item.question_text, item.pub_date)

    context = {
        'obj': Question.objects.all()
    }
    return render(request, "polls/home.html", context)

def detail_view(request, q_id):
    # try and except method
    # try:
    #     q = Question.objects.get(id=q_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question doesn't exist.")

    #shortcut
    q = get_object_or_404(Question, id=q_id)
    context = {
        "question": q
    }
    return render(request, "polls/detail.html", context)

class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'
    # q = Question.objects.get(id=q_id)
    # context = {
    #     "question": q
    # }
    # return render(request, "polls/results.html", context)

def vote_view(request, q_id):
    print(q_id, "hey vote view is called")
    print(request.POST)

    q = get_object_or_404(Question, id=q_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": q,
            "error_message": "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # return render(request, "polls/results.html", {'question': q})
        return HttpResponseRedirect(reverse('polls:result', args=(q.id, )))
