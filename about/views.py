from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm

# Create your views here.


def about_page(request):
    """
    Renders the about page with contact form.
    """
    if request.method == 'POST':
        contact = ContactForm(data=request.POST)
        if contact.is_valid():
            contact.save()
            messages.add_message(
                request, messages.SUCCESS, 'Message sent successfully.'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Message not sent. Please try again.'
            )

    about = About.objects.all().order_by('-updated').first()
    contact = ContactForm()

    return render(
        request, 'about.html',
        {
            'about': about,
            'contact': contact,
         },
    )
