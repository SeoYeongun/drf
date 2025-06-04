from rest_framework import serializers
from .models import Topic, Item, Vote

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'items']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'item', 'user', 'score', 'created_at']
        read_only_fields = ['created_at']

    def validate_score(self, value):
        value = int(value)
        if value < 1 or value > 5:
            raise serializers.ValidationError("점수는 1에서 5 사이여야 합니다.")
        return value
