from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Claim
from teams.models import Team

def index(request):
    listings = Claim.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }
    return render(request, 'claims/claims.html', context)

def claim(request, claim_id):
    listing = get_object_or_404(Claim, pk=claim_id)
    supports = Team.objects.all().filter(is_support=True)

    context = {
        'listing' : listing,
        'supports' : supports
    }
    return render(request, 'claims/claim.html', context)