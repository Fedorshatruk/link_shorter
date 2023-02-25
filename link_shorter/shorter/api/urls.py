from django.urls import include, path
from rest_framework.routers import DefaultRouter

from shorter.api.views import TokenViewSet, RedirectView

router = DefaultRouter()
router.register("api/token", TokenViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('<str:subpart>/', RedirectView.as_view())
]
