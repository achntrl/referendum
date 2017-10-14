from django.contrib import admin

from polls.models import Question, Choice


class ChoiceAdmin(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ('id', 'question',)
    list_display_links = ('id', 'question')
    inlines = (ChoiceAdmin, )


admin.site.register(Question, QuestionAdmin)
