from django.shortcuts import render
from .models import About

# Create your views here.


def about_page(request):
    """
    Renders the about page.
    """
    about = About.objects.all().order_by('-updated').first()

    return render(request, 'about.html', {'about': about})
