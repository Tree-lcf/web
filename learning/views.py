from django.shortcuts import render
from .models import Topic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    '''learning index'''
    return render(request, '../templates/learning/index.html')


def topics(request):
    '''show the topics'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, '../templates/learning/topics.html', context)


def topic(request, topic_id):
    """show the items in topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, '../templates/learning/topic.html', context)


def new_topic(request):
    """add new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning:topics'))

    context = {'form': form}
    return render(request, '../templates/learning/new_topic.html', context)


def new_entry(request, topic_id):
    """add new item for topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, '../templates/learning/new_entry.html', context)

