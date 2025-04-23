from django.urls import path
from smartcv.views import index

urlpatterns = [
    path('', index)
]