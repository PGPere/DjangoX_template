from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/spice_bazaar_home.html"
