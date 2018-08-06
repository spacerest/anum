from django.db import models

# Create your models here.

class Page(models.Model):
    page_name = models.CharField(max_length = 50)

class Section(models.Model):
    title = models.CharField(max_length = 50)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True)

class Paragraph(models.Model):
    text = models.TextField(max_length = 100000)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
