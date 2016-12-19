from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import Entries

def show_entries(request):

    if request.method == "POST":
        entry = Entries.objects.create(name=request.POST.get("entry_name"),
                            description=request.POST.get("description_name"),
                            owner=request.user)

        entry.tags.add(*request.POST.getlist("tag_names"))


    return render(request, "my_entries.html", {"entries": Entries.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all()})


def get_entries(request, entry_id):
    try:
        entry = Entries.objects.get(id=entry_id)
        if request.user.id != entry.owner.id:
            raise PermissionDenied
        return render(request, "detailed_entry.html", {"enrty": entry})
    except Entries.DoesNotExist:
        raise Http404("We don't have any.")