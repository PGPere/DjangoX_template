from django.urls import path

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="spice_bazaar_home"), ]
