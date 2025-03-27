from django.contrib import admin
from django.urls import path
from vic_app.views import SampleAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data/', SampleAPIView.as_view(), name='sample_api'),
]
