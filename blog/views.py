from django.shortcuts import render
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import blog,comment
from django.template import Context, Template
import datetime
from datetime import date,timedelta
from django import forms
from django.utils import timezone
from .forms import blogform,comentform


def index(request,date):
    date = datetime.datetime.now().date()

    return render(request, 'blog/index.html',
                  {'date': date})
