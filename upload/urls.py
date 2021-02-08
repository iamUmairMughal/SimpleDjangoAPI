from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import post
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
# router.register('books', post)

urlpatterns = [
    path('books/', post, name='post'),
    # path('img', BookViewSet.post, name= 'post'),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)