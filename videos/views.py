from django.shortcuts import render, reverse, redirect
from django.db.models import Q
from .models import Serie, Episode, SerieComments
from premium.models import user_subscription
from django.contrib.auth.models import User
import datetime

# Create your views here.


def all_videos(request):

    series = Serie.objects.all()

    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                #messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('videos'))

            queries = Q(friendly_name__icontains=query) | Q(description__icontains=query) | Q(genre__icontains=query)
            series = Serie.objects.filter(queries)

    context = {
        'series': series,
        'search_term': query,
    }

    return render(request, 'videos/videos.html', context)


def current_episode_details(request, serie_id, episode_id):

    try:
        current_user_subscription = user_subscription.objects.filter(
                                        user=request.user).values('premium_until')
        premium_date = current_user_subscription[0]['premium_until']
        now = datetime.date.today()

        if premium_date > now:
            premium = True
        else:
            premium = False

    except:
        premium = False
    current_episode = Episode.objects.filter(id=episode_id)
    episodes = Episode.objects.filter(series__id=serie_id)

    context = {
        'episodes': episodes,
        'current_episode': current_episode,
        'premium': premium
    }

    return render(request, 'videos/current_episode_details.html', context)


def current_serie_details(request, serie_id):

    episodes = Episode.objects.filter(series__id=serie_id)
    current_serie = Serie.objects.filter(id=serie_id)
    comments = SerieComments.objects.filter(Serie__id=serie_id)
    if request.method == 'POST':
        now = datetime.datetime.now()
        comment = {
            'comment': request.POST.get("new_comment"),
            'name': request.user,
            'Serie': Serie.objects.get(id=serie_id),
            'date': now
        }

        SerieComments.objects.create(**comment)

    try:
        current_user_subscription = user_subscription.objects.filter(
                                        user=request.user).values('premium_until')
        premium_date = current_user_subscription[0]['premium_until']
        now = datetime.date.today()

        if premium_date > now:
            premium = True
        else:
            premium = False

    except:
        premium = False

    serie_id = Serie.objects.filter(id=serie_id).values('id')
    context = {
        'episodes': episodes,
        'comments': comments,
        'current_serie': current_serie,
        'serie_id': serie_id,
        'premium': premium
    }

    return render(request, 'videos/current_serie_details.html', context)


def delete_comment(request, comment_id):
    serie = SerieComments.objects.filter(id=comment_id).values('Serie')
    serie_id = serie[0]['Serie']
    SerieComments.objects.filter(id=comment_id).delete()

    return (redirect(current_serie_details, serie_id))
