from rest_framework.serializers import ModelSerializer
from base.models import Room, User

# to plik w którym pliki(pythonowe obiekty) będą przekształcane w pliki json(javascript), ponieważ nie da się podawać obiektów w api

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'