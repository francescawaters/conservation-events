from django.shortcuts import render
from django.views import generic
from .models import Event
from django.shortcuts import render, get_object_or_404

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


def event_detail(request, slug):
    """
    Display an individual :model:`events.Event`.

    **Context**

    ``events``
        An instance of :model:`events.Event`.

    **Template:**

    :template:`events/event_detail.html`
    """

    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "event_detail.html",
        {"event": event},
    )
