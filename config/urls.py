from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path('ledger/', include('ledger.urls', namespace='ledger')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
