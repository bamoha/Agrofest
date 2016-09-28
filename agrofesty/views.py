from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,  Http404
from django.template import RequestContext

def index(request):
    output = '''
    <html>
    <head><title>%s</title></head>
    <body>
    <h1>%s</h1><p>%s</p>
    </body>
    </html>
    ''' % (
    'Django Bookmarks',
    'Welcome to Django Bookmarks',
    'Where you can store and share bookmarks!'
    )
    return HttpResponse(output)
