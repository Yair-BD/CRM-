from django.forms import ModelForm  
from .models import *


class LeadForm (ModelForm):
    class Meta:
        model = Lead
        fields = "__all__" 