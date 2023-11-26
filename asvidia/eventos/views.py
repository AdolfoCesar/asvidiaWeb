from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.
def eventos(request, year, month):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #calendario = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'eventos.html', {"year":year,"month":month,"month_number":month_number,})