from django.shortcuts import render
from .forms import User

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def members(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def games(request):
  template = loader.get_template('games.html')
  return HttpResponse(template.render())

def test(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = User(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/thanks/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = User()

#     return render(request, "name.html", {"form": form})
