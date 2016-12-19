from django.shortcuts import render

# Create your views here.
from .models import Tag

def show_tag(request):

    if request.method == "POST":
        Tag.objects.create(name=request.POST.get("tag_name"))

    return render(request, "my_tags.html", {"tags": Tag.objects.all()})
