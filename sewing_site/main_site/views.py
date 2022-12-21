from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

# Import the needed classes from other files.
from .forms import RequestForm
from .models import Project, Request

# Create your views here.


class IndexPage(TemplateView):
    """ Index Page
    The class returns the index page with the latest project.
    """
    # Set the template.
    template_name = "main_site/index.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the earliest project.
        try:
            projects = Project.objects.all().order_by("-last_update")
            earliest_project = projects[0]
        except:
            # If failed, return blank.
            earliest_project = []
        
        # Update and return the context.
        context["title"] = "Home"
        context["path"] = "/home"
        context["project"] = earliest_project
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


class AboutPage(TemplateView):
    """About Page
    The class delivers the view of the about page.
    """
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
    paginate_by = 6


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "List of Projects"
        context["path"] = "/projects"
        return context


class ProjectDetail(DetailView):
    """ Project Detail
    The class returns the project details page.
    """
    # Set the template.
    template_name = "main_site/project-details.html"
    model = Project


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project Details"
        context["path"] = "/projects"
        return context
