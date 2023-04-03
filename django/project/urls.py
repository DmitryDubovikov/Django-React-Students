from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from students.views import StudentViewSet
from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()
router.register(r"students", StudentViewSet, basename="students")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/swagger/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
