from django.contrib import admin
from django.urls import include, path


admin.site.site_header = 'Pennlabs Example Admin'

urlpatterns = [
    # Normal URL Patterns go here
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
