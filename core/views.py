from django.shortcuts import render
from .forms import CountriesForm
from .models import Country
from .helpers import get_laws_in_country
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    context = {

    }

    return render(request, 'core/home.html', context)

def get_started(request):
    if request.method == 'GET':
        form = CountriesForm()
    else:
        form = CountriesForm(request.POST)

        from_country = request.POST.get('from_country', '')
        to_country = request.POST.get('to_country', '')
        country = Country.objects.filter(pk=to_country)
        country_slug = ''
        for c in country:
            country_slug = c.slug
        if from_country and to_country:
            return HttpResponseRedirect(f'/country-related-laws/{country_slug}')

    context = {
        'title': 'Getting Started',
        'form': form,
        'countries': Country.objects.all()
    }

    return render(request, 'core/get-started.html', context)

def country_laws(request, slug):
    country = Country.objects.get(slug=slug)
    laws = get_laws_in_country(country.id)
    context = {
        'title': country.name,
        'laws': laws,
        'country': country
    }

    return render(request, 'core/country_laws.html', context)