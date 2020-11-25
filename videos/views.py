from django.shortcuts import render
from .models import Serie, Episode

# Create your views here.


def all_videos(request):

    series = Serie.objects.all()

    context = {
        'series': series,
    }

    return render(request, 'videos/videos.html', context)
