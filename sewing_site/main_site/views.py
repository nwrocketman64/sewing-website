from django.shortcuts import render

# Create your views here.


# The function delivers the home page.
def index_page(request):
    return render(request, "main_site/index.html", {
        "title": "Home",
        "path": "/home",
    })


# The function delivers the services page.
def services_page(request):
    return render(request, "main_site/services.html", {
        "title": "Services",
        "path": "/services",
    })
    
    
# The function delivers the contact page.
def contact_page(request):
    return render(request, "main_site/contact.html", {
        "title": "Contact Us",
        "path": "/contact",
    })


# The function delivers the about me page.
def about_page(request):
    return render(request, "main_site/about.html", {
        "title": "About Me",
        "path": "/about",
    })
