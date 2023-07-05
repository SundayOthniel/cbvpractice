from django.urls import path
from .views import list_view

urlpatterns = [
    path('', list_view.as_view()),
]