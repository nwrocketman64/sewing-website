from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index-page"),
    path("services", views.ServicesPage.as_view(), name="service-page"),
    path("contact", views.ContactPage.as_view(), name="contact-page"),
    path("about", views.AboutPage.as_view(), name="about-page"),
    path("contact-submitted", views.ContactSubmitPage.as_view(), name="contact-submitted"),
    path("projects", views.ProjectList.as_view(), name="project-list"),
    path("projects/<slug:slug>", views.ProjectDetail.as_view(), name="project-details")
]
