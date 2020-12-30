from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection,transaction
from .models import Trip
import sqlite3


# Create your views here.

@login_required
def homeView(request):
    user_id = request.user.id
    context = { 'acc_id' : user_id }
    return render(request, 'home.html', context)

@login_required
def bookingView(request):

    return render(request, 'booking.html')

@login_required
def faresView(request):
    # Flaw 2.
    acc_id = request.GET.get('accountId')

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Flaw 3.

    rows = cursor.execute("SELECT * FROM ship_trip WHERE user_id='%s'" % (acc_id))
    context = { 'trips' : dictfetchall(rows) }
    transaction.commit()
    cursor.close()
    return render(request, 'trips.html', context)

@login_required
def confirmView(request):
    trip = request.POST.get('trip')
    creditcard = request.POST.get('credit')
    date = request.POST.get('day')
    user_id = request.POST.get('accountId')
    user = User.objects.get(id=user_id)

    trip = Trip(user=user, trip=trip, date=date, creditcard=creditcard)
    trip.save()

    return redirect('/fares?accountId=' + str(user.id))

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

