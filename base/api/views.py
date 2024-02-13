from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, User
from .serializers import RoomSerializer, UserSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        '',
        'Show all rooms or specific room from room.id',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        '',
        'Show all users or specific user from user.id',
        'GET /api/users',
        'GET /api/users/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)