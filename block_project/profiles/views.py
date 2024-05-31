from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_profile(request):
    if request.method=='POST':
        profile_Forms = forms.ProfileForms(request.POST)
        if profile_Forms.is_valid():
            profile_Forms.save()
            return redirect("add_profiles")
        
    else:
        profile_Forms = forms.ProfileForms()   
    return render(request,"profiles/add_profiles.html",{'form': profile_Forms})