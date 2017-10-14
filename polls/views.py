from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice, Vote


class IndexView(generic.ListView):
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
         if len(Vote.objects.filter(
                 question_id=selected_choice.question.id,
                 voter_id=request.user.id)) > 0:
             return render(request, 'polls/question_detail.html', {
                 'question': question,
                 'error_message': "Vous avez déjà voté pour cette question",
             })

         user_vote = Vote()
         user_vote.voter = request.user.profile
         user_vote.choice = selected_choice
         user_vote.question = selected_choice.question
         user_vote.save()
         selected_choice.votes += 1
         selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/question_results.html', {'question': question})
