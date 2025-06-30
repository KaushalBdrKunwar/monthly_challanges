# from django.contrib import admin
from django.urls import path
from . import views

# urlpatterns = [
#     path('january',views.january),
#     path('february',views.february),
# ]

#3. Dyanamic url patterns
urlpatterns =[
    path('',views.index),
    path('<int:month>',views.monthly_challange_by_number),
    path('<str:month>',views.monthly_challange, name='month-challenge'),
]