from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Import the needed classes from other files.
from .forms import RequestForm
from .models import Project, Request

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
        
        
class ProjectList(ListView):
    """Project List
    The class delivers the view of the list of projects.
    """
    # Set the template, model, order by last update.
    template_name = "main_site/project-list.html"
    model = Project
    ordering = ["-last_update"]
    context_object_name = "projects"

    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "List of Projects"
        context["path"] = "/projects"
        return context
    
    
class ProjectDetail(TemplateView):
    # Set the template.
    template_name = "main_site/project-details.html"

    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project Details"
        context["path"] = "/projects"
        return context
