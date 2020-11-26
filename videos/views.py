from django.shortcuts import render, reverse, redirect
from django.db.models import Q
from .models import Serie, Episode

# Create your views here.


def all_videos(request):

    series = Serie.objects.all()
    
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                #messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('all_videos'))

            queries = Q(friendly_name__icontains=query) | Q(description__icontains=query) | Q(genre__icontains=query)
            series = Serie.objects.filter(queries)


    context = {
        'series': series,
        'search_term': query,
    }

    print(context)

    return render(request, 'videos/videos.html', context)


def current_serie_details(request, serie_id):

    episodes = Episode.objects.filter(series__id=serie_id) 

    context = {
        'episodes': episodes,
    }

    return render(request, 'videos/current_serie_details.html', context)
