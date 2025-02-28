from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, SignupView, LoginView

# Create a router and register the PlayerViewSet
router = DefaultRouter()
router.register(r'players', PlayerViewSet)  # This maps /players/ to PlayerViewSet

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),  
]
