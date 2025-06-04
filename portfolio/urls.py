from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TopicViewSet, ItemViewSet, VoteViewSet

router = DefaultRouter()
router.register('topics', TopicViewSet)
router.register('items', ItemViewSet)
router.register('votes', VoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
