from rest_framework import serializers
from api.models import Mood
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    moods = serializers.PrimaryKeyRelatedField(many=True, queryset=Mood.objects.all())

    class Meta:
        model = Profile
        fields = ['id', 'username', 'moods', 'streak']


class MoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(required=False, allow_blank=True, max_length=100)
    owner = serializers.ReadOnlyField(source='owner.username')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Mood.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance