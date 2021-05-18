
from django.shortcuts import redirect, render, HttpResponse
def index(request):
    return render(request,"home.html")

def login(request):
    context = {
    'name' :request.POST["name"],
    'DojoLocation' : request.POST["Dojo_Location"],
    'FavoriteLanguage' :request.POST["Favorite_Language"],
    'comment' : request.POST["comment"]
    }
    return render(request,'show.html' ,context)


