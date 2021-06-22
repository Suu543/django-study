import challenges
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Hello January",
    "february": "Hello February",
    "march": "Hello March",
    "april": "Hello April",
    "may": "Hello May",
    "june": "Hello June",
    "july": "Hello July",
    "august": "Hello August",
    "september": "Hello September",
    "october": "Hello October",
    "november": "Hello November",
    "december": None
}

# Create your views here.

# Keyword Arguments ==> Dynamic Path Segments
# def monthly_challenge(request, month):
#     challenge_text = None
    
#     if month == "january":
#         challenge_text = "Eat no meat for the entire month!"
#     elif month == "february":
#         challenge_text = "Walk for at least 20 minutes every day!"
#     elif month == "march":
#         challenge_text = "Learn Django for at least 20 minutes every day!"
#     else:
#         return HttpResponseNotFound("This month is not supported")
    
#     return HttpResponse(challenge_text)

# def monthly_challenges_by_number(request, month):
#     return HttpResponse(month)

# def monthly_challenges_by_number(request, month):
#     months = list(monthly_challenges.keys())
#     redirect_month = months[month]
#     return HttpResponseRedirect(f"/challenges/{redirect_month}")

# def monthly_challenges_by_number(request, month):
#     months = list(monthly_challenges.keys())
    
#     if month > len(months):
#         return HttpResponseNotFound("Invalid Month")
    
#     redirect_month = months[month - 1]
#     return HttpResponseRedirect(f"/challenge/{redirect_month}")
# def index(request):
#     list_items = ""
#     months = list(monthly_challenges.keys())

#     for month in months:
#         capitalized_month = month.capitalize()
#         month_path = reverse("month-challenge", args=[month])
#         print("month_path", month_path)
#         list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

#     response_data = f"<ul>{list_items}</ul>"
    
#     return HttpResponse(response_data)

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })



def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month]
#         response_data = f"<h1 style=color:gold;background:black;>{challenge_text}</h1>"
#         return HttpResponse(response_data)
#     except:
#         return HttpResponseNotFound("<h1>This month is not supported!</h1>")        

# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month]
#         # response_data = render_to_string("challenges/challenge.html")
#         # return HttpResponse(response_data)
#         return render(request, "challenges/challenge.html")
#     except:
#         return HttpResponseNotFound("<h1>This month is not supported!</h1>")        
    

# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month]
#         return render(request, "challenges/challenge.html", {
#             "text": challenge_text,
#             "month_name": month.capitalize()
#         })
#     except:
#         return HttpResponseNotFound("<h1>This month is not supported!</h1>")        
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # raise Http404()