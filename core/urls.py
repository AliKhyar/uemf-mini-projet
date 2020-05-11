from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home_page, name="home"),
    path("actor-movies/<actor_id>/", views.actor_movies, name="actor_movies"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)