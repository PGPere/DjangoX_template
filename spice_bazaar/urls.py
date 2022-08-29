from django.urls import path

from .views import HomePageView
from .views import SpiceDetail, SpiceList
from .views import SpiceCreateView, SpiceDeleteView, SpiceUpdateView

urlpatterns = [
    path("", HomePageView.as_view(), name="spice_bazaar_home"),
    path(' ', SpiceList.as_view(), name='spice_list'),
    path('<int:pk>', SpiceDetail.as_view(), name='spice_detail'),
    path('create/', SpiceCreateView.as_view(), name='spice-add'),
    path('<int:pk>/update/',
         SpiceUpdateView.as_view(), name='spice-update'),
    path('<int:pk>/delete/', SpiceDeleteView.as_view(), name='spice-delete'),
]
