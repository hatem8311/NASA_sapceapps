from django.conf.urls import url,include
from django.contrib import admin
from homepage import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^Rockets1/', include('homepage.urls',namespace='Rockets1')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
