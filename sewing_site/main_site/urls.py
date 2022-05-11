from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, name="index-page"),
    path("services", views.services_page, name="service-page"),
    path("contact", views.contact_page, name="contact-page"),
    path("about", views.about_page, name="about-page"),
]
