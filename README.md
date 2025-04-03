# Overview
This is the main codebase for Webb's Crafting Gallery, a website that advertises sewing services, hosts a blog, and sells sewing projects. The codebase is written in Python using Django as the web framework following the MVC architecture. The website uses Django's built-in admin interface to manage projects and images. It is designed to run on Python 3.10.5 or later and works with the latest version of Django. This codebase is free and open-source under the Apache 2.0 license. Please feel free to contribute improvements or report any issues you find.

# Installing
To install the website for running on your computer, you can clone the codebase either by using the GitHub website or through git. Once it is on your computer, to get the website running you must create an `.env` file and place it in the second sewing_site folder where the settings.py file is located.

## .env File Template
Your `.env` file should include the following settings:

```
DEBUG_SET=TRUE
SECRET_KEY=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=localhost
DATABASE_PORT=3306
TIMEZONE=
RECAP_PUBLIC_KEY=
RECAP_PRIVATE_KEY=
HTTPS=
```
Set `HTTPS=TRUE` when deploying to production to enable secure cookie settings and HSTS.

Add all the database information, set the timezone, and set Debug to FALSE in production. Run this code in the Python shell to generate a secret key:
```
from django.core.management.utils import get_random_secret_key  
print(get_random_secret_key())
```

## Installation Steps
Make sure that the latest version of Python is installed with an updated version of pip. Then, install the required packages:

```
pip3 install django pillow mysqlclient django-environ django-recaptcha django-extensions django-cleanup django-csp
```

Once the packages are installed, make sure that you have a database server installed on your computer such as MariaDB or another SQL database. After that, you'll need to migrate the database using these commands:

```
python manage.py makemigrations
```
```
python manage.py migrate --run-syncdb
```

Make sure that you include `--run-syncdb` otherwise the tables for the models won't be created. Then, create a user for the admin although this isn't required to start the website. Only if you want to use the admin section:

```
python manage.py createsuperuser
```

## Running the Website
For development:
```
python manage.py runserver
```
For development with HTTPS (using django-extensions):
```
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```
This will generate a self-signed certificate for local HTTPS testing.

# Development Environment
These are the tools that I used to help create this website.

* [VS code](https://code.visualstudio.com/) - The main IDE for creating the source code.
* [Geany](https://www.geany.org/) - A second IDE for when I couldn't use VS code.
* [Raspberry Pi Computer](https://www.raspberrypi.org/) - A credit-card size computer used for
testing and development.
* [MariaDB](https://mariadb.org/) - The database that I used for testing and development.

# Libraries Used
Some of the key Python libraries that I used for this website.

* [Django](https://www.djangoproject.com/) - The main web framework that powers the website.
* [Python Imaging Library or PIL](https://python-pillow.org/) - I used this to resize the images when they are uploaded.
* [django-environ](https://django-environ.readthedocs.io/en/latest/) - Used to load the enviroment variables.
* [django-recaptcha](https://github.com/torchbox/django-recaptcha) - Used to implement ReCaptcha for the contact form.
* [Normalize.css](https://necolas.github.io/normalize.css/) - The CSS normalizer that I use for the website.
* [django-csp](https://github.com/mozilla/django-csp) - Used to implement Content Security Policy for improved security.
* [django-extensions](https://django-extensions.readthedocs.io/) - Provides additional management commands and development tools.
* [django-cleanup](https://github.com/un1t/django-cleanup) - Automatically deletes files when models are deleted.
* [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - Provides beautiful rendering of forms.

# Useful Websites
This Udemy course is were I first learned to use Python Django.

* [Python Django - The Practical Guide](https://www.udemy.com/share/104wQs3@1bRZKG7_5UNHtevDwosC4eWZpqtrUvGa3nxuJJabAWCRZwypeSWaMlcIr1qO-duONw==/)
* [Pagination](https://docs.djangoproject.com/en/4.1/topics/pagination/)

# Change Log
* 1.3.0 - Updated Django to 5.2, enabled HSTS and CSP. 4/3/2025
* 1.2.1 - Updated Packages, fixed issue with models. 3/7/2025
* 1.2.0 - Updated Django, Added Django Cleanup, cleaned up code in model and template. 1/14/2025
* 1.1.18 - Updated Django. 8/6/2024
* 1.1.17 - Updated Django. 7/9/2024
* 1.1.16 - Updated Django. 5/27/2024
* 1.1.15 - Updated Django. 4/5/2024
* 1.1.14 - Updated Django and mysqlclient. 3/7/2024
* 1.1.13 - Updated Django to 5.0.2. 2/7/2024
* 1.1.12 - Updated Django an other Python packages. 2/4/2024
* 1.1.11 - Updated Django to current version. 9/9/2023
* 1.1.10 - Added a venv so website could run on the current version of Ubuntu Server. 7/27/2023
* 1.1.9 - Updated Python Django to version 4.2. 4/3/2023
* 1.1.8 - Prevent textarea in contact form from being resizeable. 2/16/2023
* 1.1.7 - Removed label for ReCaptcha on the Contact Form page. 12/22/2022
* 1.1.6 - Updated Project details page, Added paging to the Project list page. 12/21/2022
* 1.1.5 - Update the home page, change the appearance of the button, updated the packages to Django 4.1.3. 11/10/2022
* 1.1.4 - Compressed CSS files. Updated packages to Django 4.1.2. 10/22/2022
* 1.1.3 - Updated packages to Django 4.1, implemented Google's ReCaptcha to reduce Bots and Spam on the Contact Form page. 8/19/2022
* 1.1.2 - Updated the Home, Services, and About page. 7/14/2022
* 1.1.1 - Fixed issues with images not having EXIF metadate being saved correctly, Fixed issue with slide container not having the correct box shadow. 7/6/2022
* 1.1.0 - Fixed issues with headers, added box shadow for images slides, fixed error from slide JavaScript file, updated home page header, updated about page. 7/1/2022
* 1.0.0 - Website Completed and first deployment. 6/28/2022

# Website Link
This is the link to the deployed website.

[Webb's Crafting Gallery](https://www.webbcraftinggallery.com/)
