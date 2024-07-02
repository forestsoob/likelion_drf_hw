from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer']

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    
    songs = serializers.SerializerMethodField(read_only=True)

    def get_songs(self, instance):
        # Singer 객체와 연결된 Song 객체들을 가져오기 위해
        # instance.songs.all()로 관계된 Song 객체들을 가져옵니다.
        songs = instance.songs.all()
        serializer = SongSerializer(songs, many=True)
        return serializer.data

    class Meta:
        model = Singer
        fields = '__all__'