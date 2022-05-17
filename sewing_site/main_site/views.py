from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

# Import the needed classes from other files.
from .forms import RequestForm
from .models import Request

# Create your views here.


# The class delivers the home page.
class IndexPage(TemplateView):
    # Set the template.
    template_name = "main_site/index.html"

    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        context["path"] = "/home"
        return context


# The class delivers the services page.
class ServicesPage(TemplateView):
    # Set the template.
    template_name = "main_site/services.html"

    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Services"
        context["path"] = "/services"
        return context


class ContactPage(CreateView):
    """ Contact Page
    The class renders the contact view page based off of the request
    model.
    """
    # Set the template, model, form, and url redirect.
    template_name = "main_site/contact.html"
    model = Request
    form_class = RequestForm
    success_url = "/contact-submitted"

    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact Us"
        context["path"] = "/contact"
        return context


class ContactSubmitPage(TemplateView):
    """Contact Submit Page
    The class renders the contact success submit page.
    """
    # Set the template.
    template_name = "main_site/contact-submit.html"

    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact Us"
        context["path"] = "/contact"
        return context


# The class delivers the about me page.
class AboutPage(TemplateView):
    # Set the template.
    template_name = "main_site/about.html"

    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Me"
        context["path"] = "/about"
        return context
