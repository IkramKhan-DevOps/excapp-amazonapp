from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.website.urls', namespace='website')),
    path('accounts/', include('Apps.accounts.urls', namespace='accounts'))
]
