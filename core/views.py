from django.shortcuts import render
from .models import Film, Actor

# Create your views here.



def home_page(request):
    films = Film.objects.all()
    actors = Actor.objects.all()
    carousel_images = [films[0].poster, films[1].poster, actors[0].picture]

    context = {
        "films":films,
        "actors":actors,
        "carousel_images":carousel_images,
    }

    return render(request,
                  template_name="core/home.html",
                  context=context
                  )

def actor_movies(request,actor_id):
    actor = Actor.objects.filter(id=actor_id)[0]
    films = Film.objects.filter(actor = actor_id)
    context = {
        'actor':actor,
        'films':films,
    }
    return render(request,
                  template_name="core/actor_movies.html",
                  context=context
                  )