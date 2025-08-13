from django.views.generic import TemplateView


class WelcomeToSpeedPyView(TemplateView):
    template_name = "mainapp/welcome.html"


    def get(self, request, *args, **kwargs):
        print(request.META)
        return super().get(request, *args, **kwargs)


class PricingView(TemplateView):
    template_name = "mainapp/pricing.html"
