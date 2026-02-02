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


def team(request):
    message = None
    created_team = None

    if request.method == "POST":
        team_name = (request.POST.get("teamName") or "").strip()
        captain = (request.POST.get("cap") or "").strip()
        trophy = (request.POST.get("trophy") or "").strip()
        raw_players = (request.POST.get("playerList") or "").strip()

        # Accept comma-separated and/or newline-separated players
        players = []
        for chunk in raw_players.replace(",", "\n").splitlines():
            name = chunk.strip()
            if name:
                players.append(name)

        if len(players) < 5:
            message = "Add at least 5 players to create a team."
        else:
            created_team = {
                "teamName": team_name,
                "cap": captain,
                "trophy": trophy,
                "playerList": players,
            }

            # Store created teams in session ("own" section)
            teams = request.session.get("teams", [])
            teams.append(created_team)
            request.session["teams"] = teams

    context = {
        "message": message,
        "created_team": created_team,
        "own_teams": request.session.get("teams", []),
    }
    return render(request, "team.html", context)