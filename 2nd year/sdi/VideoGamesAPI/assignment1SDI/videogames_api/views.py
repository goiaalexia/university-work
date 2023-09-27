import math

from django.db.models import Avg
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

"""
API Views for the Video Games
"""


class VideoGameListApiView(APIView):

    # 1. List all video games
    def get(self, request, *args, **kwargs):
        """
        List all the video games that can be seen.
        """
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        videogames = VideoGame.objects.all()
        total_movies = videogames.count()
        if search_param:
            videogames = videogames.filter(title__icontains=search_param)
        serializer = VideoGameSerializer(
            videogames[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_movies,
            "page": page_num,
            "last_page": math.ceil(total_movies / limit_num),
            "videogames": serializer.data
        })

    # 2. Create new video game
    def post(self, request, *args, **kwargs):
        """
        Create the video game with given data
        """
        data = {
            'name': request.data.get('name'),
            'releaseYear': request.data.get('releaseYear'),
            'company': request.data.get('company'),
            'platform': request.data.get('platform'),
            'rating': request.data.get('rating'),
            'sales': request.data.get('sales'),
        }
        serializer = VideoGameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoGameDetailApiView(APIView):
    # no.
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, videogame_id):
        """
        Helper method to get the object with given game_name, and user_id
        """
        try:
            return VideoGame.objects.get(id=videogame_id)
        except VideoGame.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, videogame_id, *args, **kwargs):
        """
        Retrieves the video game with given game_name
        """
        videogame_instance = self.get_object(videogame_id)
        if not videogame_instance:
            return Response(
                {"res": "Object with game name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = VideoGameSerializer(videogame_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, videogame_id, *args, **kwargs):
        """
        Updates the todo item with given todo_id if exists
        """
        videogame_instance = self.get_object(videogame_id)
        if not videogame_instance:
            return Response(
                {"res": "Object with game name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'releaseYear': request.data.get('releaseYear'),
            'company': request.data.get('company'),
            'platform': request.data.get('platform'),
            'rating': request.data.get('rating'),
            'sales': request.data.get('sales'),
            'players': request.data.get('players')
        }
        serializer = VideoGameSerializer(instance=videogame_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, videogame_id, *args, **kwargs):
        """
        Deletes the video game with given game_name if exists
        """
        videogame_instance = self.get_object(videogame_id)
        if not videogame_instance:
            return Response(
                {"res": "Object with game name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        videogame_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class PlatformListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all platforms
    def get(self, request, *args, **kwargs):
        """
        List all the platforms that can be seen.
        """
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        platforms = Platform.objects.all()
        total_movies = platforms.count()
        if search_param:
            platforms = platforms.filter(title__icontains=search_param)
        serializer = PlatformSerializer(
            platforms[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_movies,
            "page": page_num,
            "last_page": math.ceil(total_movies / limit_num),
            "videogames": serializer.data
        })

    # 2. Create new platform
    def post(self, request, *args, **kwargs):
        """
        Create the platform with given data
        """
        data = {
            'name': request.data.get('name'),
            'activeUsers': request.data.get('activeUsers'),
            'screen': request.data.get('screen'),
            'handheld': request.data.get('handheld'),
            'size': request.data.get('size')
        }
        serializer = PlatformSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlatformDetailApiView(APIView):

    def get_object(self, platform_id):
        """
        Helper method to get the object with given game_name, and user_id
        """
        try:
            return Platform.objects.get(id=platform_id)
        except Platform.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, platform_id, *args, **kwargs):
        """
        Retrieves the video game with given game_name
        """
        platform_instance = self.get_object(platform_id)
        if not platform_instance:
            return Response(
                {"res": "Object with platform name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PlatformSerializer(platform_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, platform_id, *args, **kwargs):
        """
        Updates the platform object if exists
        """
        platform_instance = self.get_object(platform_id)
        if not platform_instance:
            return Response(
                {"res": "Object with game name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'activeUsers': request.data.get('activeUsers'),
            'screen': request.data.get('screen'),
            'handheld': request.data.get('handheld'),
            'size': request.data.get('size')
        }
        serializer = PlatformSerializer(instance=platform_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, platform_id, *args, **kwargs):
        """
        Deletes the video game with given game_name if exists
        """
        platform_instance = self.get_object(platform_id)
        if not platform_instance:
            return Response(
                {"res": "Object with game name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        platform_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class PlayerListApiView(APIView):

    # 1. List all platforms
    def get(self, request, *args, **kwargs):
        """
        List all the platforms that can be seen.
        """
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        players = Player.objects.all()
        total_movies = players.count()
        if search_param:
            players = players.filter(title__icontains=search_param)
        serializer = PlayerSerializer(
            players[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_movies,
            "page": page_num,
            "last_page": math.ceil(total_movies / limit_num),
            "videogames": serializer.data
        })

    # 2. Create new platform
    def post(self, request, *args, **kwargs):
        """
        Create the platform with given data
        """
        data = {
            'username': request.data.get('username'),
            'age': request.data.get('age'),
            'email': request.data.get('email'),
            'gender': request.data.get('gender'),
            'favouriteGenre': request.data.get('favouriteGenre')
        }
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerDetailApiView(APIView):

    def get_object(self, player_id):
        """
        Helper method to get the object with given game_name, and user_id
        """
        try:
            return Player.objects.get(id=player_id)
        except Player.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, player_id, *args, **kwargs):
        """
        Retrieves the video game with given game_name
        """
        player_instance = self.get_object(player_id)
        if not player_instance:
            return Response(
                {"res": "Object with player name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PlayerSerializer(player_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, player_id, *args, **kwargs):
        """
        Updates the player object if exists
        """
        player_instance = self.get_object(player_id)
        if not player_instance:
            return Response(
                {"res": "Object with player name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'username': request.data.get('username'),
            'age': request.data.get('age'),
            'email': request.data.get('email'),
            'gender': request.data.get('gender'),
            'favouriteGenre': request.data.get('favouriteGenre'),
            'games': request.data.get('games')
        }
        serializer = PlayerSerializer(instance=player_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, player_id, *args, **kwargs):
        """
        Deletes the video game with given game_name if exists
        """
        player_instance = self.get_object(player_id)
        if not player_instance:
            return Response(
                {"res": "Object with player name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        player_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class SaveFileListApiView(APIView):

    # 1. List all platforms
    def get(self, request, *args, **kwargs):
        """
        List all the platforms that can be seen.
        """
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        playersgames = PlayerGame.objects.all()
        total_movies = playersgames.count()
        if search_param:
            players = playersgames.filter(title__icontains=search_param)
        serializer = PlayerGameSerializer(
            playersgames[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_movies,
            "page": page_num,
            "last_page": math.ceil(total_movies / limit_num),
            "videogames": serializer.data
        })

    # 2. Create new platform
    def post(self, request, *args, **kwargs):
        """
        Create the platform with given data
        """
        data = {
            'username': request.data.get('username'),
            'gamename': request.data.get('gamename'),
            'hoursPlayed': request.data.get('hoursPlayed'),
            'hasSaveFile': request.data.get('hasSaveFile'),

        }
        serializer = PlayerGameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaveFileDetailApiView(APIView):

    def get_object(self, playergame_id):
        """
        Helper method to get the object with given game_name, and user_id
        """
        try:
            return PlayerGame.objects.get(id=playergame_id)
        except PlayerGame.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, playergame_id, *args, **kwargs):
        """
        Retrieves the video game with given game_name
        """
        playergame_instance = self.get_object(playergame_id)
        if not playergame_instance:
            return Response(
                {"res": "Object with player name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PlayerGameSerializer(playergame_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, playergame_id, *args, **kwargs):
        """
        Updates the player object if exists
        """
        playergame_instance = self.get_object(playergame_id)
        if not playergame_instance:
            return Response(
                {"res": "Object with player name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'username': request.data.get('username'),
            'gamename': request.data.get('gamename'),
            'hoursPlayed': request.data.get('hoursPlayed'),
            'hasSaveFile': request.data.get('hasSaveFile'),
        }
        serializer = PlayerGameSerializer(instance=playergame_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, playergame_id, *args, **kwargs):
        """
        Deletes the video game with given game_name if exists
        """
        playergame_instance = self.get_object(playergame_id)
        if not playergame_instance:
            return Response(
                {"res": "Object with player name does not exist!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        playergame_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class VideoGameFilter(generics.ListAPIView):
    serializer_class = VideoGameSerializer

    # Return all videogames playable on a certain platform
    def get_queryset(self):
        return VideoGame.objects.filter(platform=self.kwargs['val'] <= 5)


class VideoGamesAverageYearStatistic(generics.ListCreateAPIView):
    serializer_class = VideoGameSerializer

    def get_queryset(self):
        query = VideoGame.objects.annotate(
            game_avg_year=Avg('releaseYear')).order_by('-game_avg_year')

        return query


class PlayersAverageAgeStatistic(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        query = Player.objects.annotate(
            player_avg_age=Avg('age')
        ).order_by('-player_avg_age')

        return query


class MultiplePlatformsView(APIView):
    @csrf_exempt
    @api_view(['POST'])
    def bulkAdd(request):
        platform_id_new_list = request.data.get('platform_id_new_list')

        # Loop through the list of videogame ids and new platforms to update
        for item in platform_id_new_list:
            videogame = VideoGame.objects.get(name=item['name'])
            videogame.platform = Platform.objects.get(Platform=item['id'])
            videogame.save()

        return Response({'message': 'Platforms updated successfully.'})


"""
 {"platform_id_new_list": [{
        "name": "Dead By Deadlight",
        "releaseYear": 2020,
        "company": "idk",
        "rating": null,
        "sales": null,
        "platform": 1
    },
    {
        "name": "Pokemon Pearl",
        "releaseYear": 2016,
        "company": "Gamefreak",
        "rating": null,
        "sales": null,
        "platform": 2
    }]
}"""
