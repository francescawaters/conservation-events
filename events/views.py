from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.

class EventList(generic.ListView):
    """
    Returns all published posts in :model:`events.Event`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`events.Event`
    ``paginate_by``
        Number of events per page.

    **Template:**

    :template:`blog/index.html`
    """
    queryset = Event.objects.filter(status=1)
    template_name = "index.html" 
    paginate_by = 6
