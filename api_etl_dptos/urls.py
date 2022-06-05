from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('transformer/', include('trannsformer.urls')),
    path('admin/', admin.site.urls),
]