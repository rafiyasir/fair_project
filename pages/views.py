from django.shortcuts import render

from .models import Page
from teams.models import Team
from claims.models import Claim

def index(request):
    contents = Page.objects.all()
    claims = Claim.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'contents' : contents,
        'claims':claims
    }

    return render(request, 'pages/index.html', context)

def about(request):
    contents = Page.objects.all()
    teams = Team.objects.all()
    supports = Team.objects.all().filter(is_support=True)

    context = {
        'contents' : contents,
        'teams' : teams,
        'supports':supports
    }

    return render(request, 'pages/about.html', context)