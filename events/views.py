from django.shortcuts import render, get_object_or_404, reverse 
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Comment
from .forms import CommentForm

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

    :template:`event_detail.html`
    """

    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    comments = event.comments.all().order_by("-created_on")
    comment_count = event.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.author = request.user
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "event_detail.html",
        {
            "event": event,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete'
                                                      ' your own comments!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))
