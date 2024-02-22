# Import necessary modules and classes from Django
from django.shortcuts import render
from django.http import HttpResponse

# Import choices (presumably constants) from a module named 'choices'
from listings.choices import price_choices, bedroom_choices, state_choices

# Import models from the 'listings' and 'realtors' apps
from listings.models import Listing
from realtors.models import Realtor

# Define a view function for the index page
def index(request):
    # Retrieve three most recent published listings and order them by list date
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    # Create a context dictionary containing necessary data for rendering the template
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # Render the 'index.html' template with the given context and return the HttpResponse
    return render(request, 'pages/index.html', context)

# Define a view function for the about page
def about(request):
    # Retrieve all realtors and order them by hire date
    realtors = Realtor.objects.order_by('-hire_date')

    # Retrieve all realtors who are marked as MVP (Most Valuable Professional)
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    # Create a context dictionary containing necessary data for rendering the template
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    # Render the 'about.html' template with the given context and return the HttpResponse
    return render(request, 'pages/about.html', context)
