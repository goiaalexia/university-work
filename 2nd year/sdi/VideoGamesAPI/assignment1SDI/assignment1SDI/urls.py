from django.contrib import admin
from django.urls import path, include

from videogames_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('videogames/', VideoGameListApiView.as_view()),
    path('videogames/<str:videogame_id>/', VideoGameDetailApiView.as_view()),  # asta
    path('videogames/filter/<int:val>', VideoGameFilter.as_view()),
    path('platforms/', PlatformListApiView.as_view()),
    path('platforms/<str:platform_id>/', PlatformDetailApiView.as_view()),
    path('players/', PlayerListApiView.as_view()),
    path('players/<str:player_id>', PlayerDetailApiView.as_view()),
    path('savefiles/', SaveFileListApiView.as_view()),
    path('savefiles/<str:playergame_id>', SaveFileDetailApiView.as_view()),
    path('videogames/by-avg-year', VideoGamesAverageYearStatistic.as_view(), name='by-avg-year'),
    path('players/by-avg-age', PlayersAverageAgeStatistic.as_view(), name='by-avg-age'),
    path('multipleplatformsbulkadd', MultiplePlatformsView.bulkAdd)
]
