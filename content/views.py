from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Experiment, Content, Vote

def get_user(u_id):
    return User.objects.get(id=u_id)

# Create your views here.

def index(request):
    """Link to the different experiments"""
    experiments = Experiment.objects.order_by('-id')
    context = {'experiments': experiments}

    return render(request, 'content/index.html', context)

def experiment(request, experiment_id):
    """
    Specification:
        Display a content the user has not voted on.
        Display checkboxes with the posible labels for the experiment
        Display a save button which registers a vote to the db and refreshes the page with a new content
    """
    user_voted_contents = [content['content_id'] for content in list(Vote.objects.filter(user_id=request.user.id).values('content_id').distinct('content_id'))]
    contents = Content.objects.filter(experiment__id=experiment_id).exclude(id__in=user_voted_contents)
    if len(contents)>0:
        assigned_content = contents[0]
    else:
        return HttpResponse('No more contents') #TODO: render No more contents, link to homepage
    context = {'content': assigned_content}
    print (context['content'])
    return render(request, 'content/experiment.html', context)

def vote(request, content_id):
    """
    Check that the user hasn't voted on this content before
    Create a vote for the content_id using vote value"""
    user = get_user(request.user.id)
    content = Content.objects.get(id=content_id)
    if Vote.objects.filter(user_id=request.user.id).filter(content_id=content_id).exists():
        return HttpResponse('you already voted') #redirect
    else:
        if request.POST['vote']=='yes':
            v = Vote(user=user, content=content, value=True)
        elif request.POST['vote']=='no':
            v = Vote(user=user, content=content, value=False)
        v.save()
        return HttpResponseRedirect(reverse('content:experiment_detail', args=(content.experiment_id,)))

