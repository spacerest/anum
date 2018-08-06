from django import forms
from django.forms import ModelForm
from website.models import *

class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ('title',)  

class ParagraphForm(ModelForm):
    class Meta:
        model = Paragraph
        fields = ('text','section',)
