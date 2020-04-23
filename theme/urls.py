from django.urls import path
from theme.views import Index

urlpatterns = [
    path('index/', Index.as_view()),
]