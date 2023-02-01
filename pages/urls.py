from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import my_view
from rest_framework_simplejwt import views as jwt_views

from .views import (
    AboutPageView,
    HomePageView,
    SnackListView,
    SnackDetailView,
    SnackUpdateView,
    SnackCreateView,
    SnackDeleteView,
    # SnackAPIDetailView,
    # SnackAPIListView,
    SnackViewSet
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api', SnackViewSet)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('create/', my_view, name='create'),
    path('snacks/', SnackListView.as_view(), name='list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='update'),
    # path('create/', SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='delete'),
    # path('<int:pk>/', SnackAPIDetailView.as_view(), name='detail'),
    # path('', SnackAPIListView.as_view(), name='list'),
    path('api/', SnackViewSet.as_view({'get': 'list', 'post': 'create'}), name='api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh')

]
