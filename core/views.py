from django.shortcuts import render
from .forms import CountriesForm
from .models import Country

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



    context = {
        'title': 'Getting Started',
        'form': form,
        'countries': Country.objects.all()
    }

    return render(request, 'core/get-started.html', context)