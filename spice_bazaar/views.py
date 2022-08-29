from django.views.generic import TemplateView
from spice_bazaar.models import Spice_bazaar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "pages/spice_bazaar_home.html"


class SpiceList(ListView):
    template_name = "spice_list.html"
    model = Spice_bazaar
    context_object_name = 'sp_list'


class SpiceDetail(DetailView):
    template_name = "spice_detail.html"
    model = Spice_bazaar


class SpiceCreateView(CreateView):
    template_name = 'spice-add.html'
    model = Spice_bazaar
    fields = ['name', 'description', 'purchaser']


class SpiceUpdateView(UpdateView):
    template_name = 'spice-update.html'
    model = Spice_bazaar
    fields = ['name', 'description', 'purchaser']


class SpiceDeleteView(DeleteView):
    template_name = 'spice-delete.html'
    model = Spice_bazaar
    success_url = reverse_lazy('spice_list')
