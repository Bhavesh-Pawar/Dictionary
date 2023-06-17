from django.urls import path
from dictionary_app.views import *


urlpatterns = [
    path('',HomeView.as_view(),name='home')
]
