from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (IngredientViewSet, RecipeViewSet, SubscribeViewSet,
                    TagViewSet, UserViewSet)

app_name = "api"

router = DefaultRouter()

router.register("users", UserViewSet, basename="user")
router.register(
    r"users/(?P<id>\d+)/subscribe",
    SubscribeViewSet,
    basename="subscribe"
)

router.register("tags", TagViewSet, basename="tag")
router.register("ingredients", IngredientViewSet, basename="ingredient")
router.register("recipes", RecipeViewSet, basename="recipe")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
