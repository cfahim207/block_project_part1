from django.shortcuts import render,redirect
from .import forms

# Create your views here.

def add_author(request):
    if request.method=='POST':
        author_form = forms.AuthorForms(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("add_auhtor")
        
    else:
        author_form = forms.AuthorForms()   
    return render(request,"author/add_author.html",{'form':author_form})
