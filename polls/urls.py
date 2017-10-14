from django.conf.urls import url

from polls.views import DetailView, IndexView, results, vote

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='polls_list'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='poll_detail'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),

]
