from rest_framework import viewsets
from .models import Topic, Item, Vote
from .serializers import TopicSerializer, ItemSerializer, VoteSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 현재 로그인한 사용자로 저장