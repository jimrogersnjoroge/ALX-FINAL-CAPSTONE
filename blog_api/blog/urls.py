from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, UserViewSet, CategoryViewSet, TagViewSet

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]