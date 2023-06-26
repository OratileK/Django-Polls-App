from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
# polls/views.py

def index(request):
    return render(request, "polls/index.html")

@login_required(login_url="/user_auth/")
def poll(request):
    print(request.user)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

#@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if not request .user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login") + "?next="+request)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing with POST data.
    # This prevents data from being posted twice if a user hits the Back button.
    return HttpResponseRedirect(
        reverse('polls:results', args=(question_id,))
        )
def about(request):
    return render(request, 'about.html')
def bootstrap(request):
    return render(request, 'bootstrap.html')
def inndexx(request):
    return render(request, 'inndexx.html')


