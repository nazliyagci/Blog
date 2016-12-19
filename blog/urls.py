from django.conf.urls import url

from blog.views import show_entries, get_entries

urlpatterns = [
    url(r'^entries$', show_entries),
    url(r'^entries/(?P<entry_id>[0-9]+)/$', get_entries),
]