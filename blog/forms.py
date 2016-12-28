from django import forms
from .models import Entries

class EntriesForm(forms.ModelForm):

    class Meta:
        model = Entries
        fields = ["name", "description", "tags"]