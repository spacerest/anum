from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from website.models import *
from website.forms import *


# Create your views here.

def index(request):
    pages = Page.objects.all()
    sections = Section.objects.all()#filter(page = 'home')
    if request.POST.get('title'):
        section_form = SectionForm(request.POST)
        if section_form.is_valid():
            title = section_form.cleaned_data.get('title')
            section = Section(title=title, page=Page.objects.filter(page_name="home")[0])
            section.save()
            section_form = SectionForm()
            paragraph_form = ParagraphForm()
        else:
            section_form = SectionForm(request.POST)
            paragraph_form = ParagraphForm()
    elif request.POST.get('text'):
        paragraph_form = ParagraphForm(request.POST)
        print(paragraph_form)
        print(request)
        print(request.POST.get('section').title)
        if paragraph_form.is_valid():
            text = paragraph_form.cleaned_data.get('text')
            section = paragraph_form.cleaned_data.get('section')
            print(section)
            paragraph = Paragraph(text=text, section=section)
            paragraph.save()
            section_form = SectionForm()
            paragraph_form = ParagraphForm()
        else:
            section_form = SectionForm()
            paragraph_form = ParagraphForm(request.POST)
    else:
        section_form = SectionForm()
        paragraph_form = ParagraphForm()
    return render(request, 'base.html', {'paragraph_form': paragraph_form, 'section_form': section_form, 'pages': pages, 'sections': sections})

@login_required(login_url='/login')
def edit_index(request):
    return render(request, 'base.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/login')
