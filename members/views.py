from django.shortcuts import render
from .forms import User

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import os
import json

def members(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def games(request):
  image_folder = 'members/static/assests/games'  # Path to your static folder
  image_files = [(f'game{cnt}', os.path.join('assests/games', i)) for cnt, i in enumerate(os.listdir(image_folder), start=1)]

  ids = [f'game{i+1}' for i in range(len(image_files))]

  with open("members/static/games_links.json", "r") as f:
    games_links = json.load(f)

  context = {
    "pics" : range(1, 17),
    'image_files': image_files,
    'game_links': zip(games_links, ids),
    }

  return render(request, 'games.html', context)

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
