from django.urls import path

from .views import add_cat_view
from .views import cat_stats_view


urlpatterns = [
    path("", add_cat_view),
    path("cat_stats/", cat_stats_view)
    ]
