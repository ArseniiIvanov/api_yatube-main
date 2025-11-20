from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views

router = DefaultRouter()
router.register('follow', views.FollowViewset, basename="follow")
router.register('posts', views.PostViewset, basename="post")

posts_router = routers.NestedDefaultRouter(
    router, 'posts', lookup='post'
)
posts_router.register(
    'comments', views.CommentViewset, basename='post-comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(posts_router.urls)),
]
