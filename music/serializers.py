from rest_framework import serializers
from .models import *

class SingerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingerImage
        fields = '__all__'
        
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

    images = SingerImageSerializer(many=True, read_only=True)

    def get_songs(self, instance):
        # Singer 객체와 연결된 Song 객체들을 가져오기 위해
        # instance.songs.all()로 관계된 Song 객체들을 가져옵니다.
        songs = instance.songs.all()
        serializer = SongSerializer(songs, many=True)
        return serializer.data
    
    tag = serializers.SerializerMethodField()
    def get_tag(self, instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]

    class Meta:
        model = Singer
        fields = '__all__'

    image = serializers.ImageField(use_url=True, required=False)

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
