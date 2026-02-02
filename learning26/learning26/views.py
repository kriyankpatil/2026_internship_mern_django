from django.http import HttpResponse
from django.shortcuts import render

#specifi url
def test(request):
    return HttpResponse("Hello")

# def AboutUs(request):
#     return HttpResponse("About")

def AboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")

def reacp(request):
    return render(request,"reacp.html")

def recipe(request):
    ingredient = ["maggie","tomato"]
    data = {"name":"maggie","time":20,"ingredient":ingredient} 
    return render(request,"recipe.html",data)

def movies(request):
    return render(request, "movies.html")

def shows(request):
    return render(request, "shows.html")

def news(request):
    return render(request, "news.html")