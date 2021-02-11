from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.
def index(request) -> HttpResponse:
    now = datetime.datetime.now()
    html = "<html><body>it is now %s. </body></html>" % now
    # return HttpResponse("hello")
    return HttpResponse(html)
