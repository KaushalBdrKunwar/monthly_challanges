from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# def january(request):
#     return HttpResponse('Eat no meat for the entire month!')

# def february(request):
#     return HttpResponse('Walk for at least 20 minutes every day!')

# def march(request):
#     return HttpResponse('Learn Django for at least 20mins every day')

monthly_challenges = {
    'january' : 'Eat no meat for the entire month!',
    'february' : 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Learn Django for at least 20 minutes every day!',
    'may': 'Learn Django for at least 20 minutes every day!',
    'june': 'Learn Django for at least 20 minutes every day!',
    'july': 'Learn Django for at least 20 minutes every day!',
    'august': 'Learn Django for at least 20 minutes every day!',
    'september': 'Learn Django for at least 20 minutes every day!',
    'october': 'Learn Django for at least 20 minutes every day!',
    'november': 'Learn Django for at least 20 minutes every day!',
    'december': 'Learn Django for at least 20 minutes every day!',
}

def index(request):
    month_list = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge',args=[month])
        month_list += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f'<ul>{month_list}</ul>'
    return HttpResponse(response_data)

#4. Monthly challenge by number
def monthly_challange_by_number(request,month):
    months = list(monthly_challenges.keys()) 

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) # /january
    return HttpResponseRedirect(redirect_path)

#-----3----------------------------------------#####

# #3. Dynamic Captured View
# def monthly_challange(request,month):
#     text = None
#     if month == 'january':
#         text= 'Eat no meat for the entire month!'
#     elif month == 'february':
#         text = 'Walk for at least 20 minutes every day!'
#     elif month == 'march':
#         text = 'Learn Django for at least 20 mins every day!'
#     else:
#         return HttpResponseNotFound('Please Provide Valid Month!')
    
#     return HttpResponse(text)

#------------5-----------------------###


def monthly_challange(request,month):
    try:
        text = monthly_challenges[month]
        response_data = f"<h1>{text}</h1>"
        return HttpResponse(response_data)
    
    except:
        return HttpResponseNotFound('<h1>The month doesnot exist!</h1>')