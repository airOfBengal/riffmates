from django.urls import path

from . import views as home_views

urlpatterns = [
    path("credits/", home_views.credits, name='credits'),
    path("about/", home_views.about, name='about'),
    path("version/", home_views.version_info, name='version'),
]
