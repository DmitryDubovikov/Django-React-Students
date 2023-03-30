from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from students.views import StudentViewSet
from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()
router.register(r"students", StudentViewSet, basename="students")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
