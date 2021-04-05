from django.shortcuts import render
from django.http import HttpResponse

from .models import Experiment, Content

# Create your views here.

def index(request):
    """Link to the different experiments"""
    experiments = Experiment.objects.order_by('-id')[:5]
    context = {'experiments': experiments}

    return render(request, 'content/index.html', context)

def experiment(request, experiment_id):
    """List 5 contents from the experiment (eventually we can order by conflicting votes)"""
    contents = Content.objects.filter(experiment__id=experiment_id).order_by('-id')[:10]
    context = {'content_list': contents}
    return render(request, 'content/experiment.html', context)

#def label(request):
    #contents = 
#def content(request, content_id):
    #return HttpResponse("You're viewing content number %s" % content_id)

