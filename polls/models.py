from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import UserProfile


class Question(models.Model):
    question = models.CharField(_('question'), max_length=200, blank=False)
    description = models.TextField(_('description'), max_length=500, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(_('choice'), max_length=200)
    votes = models.IntegerField(default=0)
    voters = models.ManyToManyField(UserProfile, through='Vote',
                                    through_fields=('choice', 'voter'))


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
