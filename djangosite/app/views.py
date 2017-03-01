from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os
from forms import MomentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
def welcome(request):
    return HttpResponse("<h1>Welcome to my site</h1>")


def moment_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            return HttpResponseRedirect(reverse("app.views.welcome"))
    else:
        form = MomentForm()
    PROJECT_ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request,os.path.join(PROJECT_ROOT,'app/templates','moment_input.html'),{'form':form})
