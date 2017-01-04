from django.conf.urls import url

from blog.views import show_entries, get_entries, show_all_entries_from_user, show_all_entries

urlpatterns = [
    url(r'^entries$', show_entries),
    url(r'^entries/(?P<entry_id>[0-9]+)/$', get_entries),
    url(r'^entries/all/user$', show_all_entries),
    url(r'^entries/user/(?P<userId>[0-9]+)$', show_all_entries_from_user),
]