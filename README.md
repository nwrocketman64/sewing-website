# Overview
This is the main codebase for the my a website that advertises sewing services as well blog / sell sewing projects. The codebase is mostly written in the Python programming language and I uses Django as the web framework. This website follows the MVC architecture for its overall structure. The website uses the built-in admin in order to add projects and images. This website is designed to used with the latest Python interpeter, which at the time is 3.10.5, although it can work with older interpeters. This website is also designed to work with the latest version of Django, which at the time is 4.05. I have made this website's codebase free and opensource under the Apache 2.0 license. Please feel free to copy and make your own changes and improvements and let me know if you find any issues with the codebase.

# Installing
To install the website for running on your computer, you can clone the codebase either by using the GitHub website or through git. Once it is on your computer, to get the website running you must create an .env and place it in the second sewing_site folder where the settings.py file is located. You must have values set in the .env file for DEBUG_SET, SECRET_KEY, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, TIMEZONE, RECAP_PUBLIC_KEY, and RECAP_PRIVATE_KEY. You must also make sure that the latest version of Python is installed with an updated version of pip. Then, make sure that these packages are installed.
```
pip3 install django pillow mysqlclient django-environ django-recaptcha
```
Once it is done installing, make sure that you have a database server install on you computer
such MariaDB or another SQL database. After that, you'll need to migrate the database using
these commands.
```
python manage.py makemigrations
```
```
python manage.py migrate --run-syncdb
```
Make sure that you include --run-syncdb otherwise the tables for the models won't be created.
Then, make sure that you create a user for the admin although this isn't required to start
the website. Only if you want to use the admin section.
```
python manage.py createsuperuser
```
After that, the website should be able to run and you can run it using this command.
```
python manage.py runserver
```

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

# Useful Websites
This Udemy course is were I first learned to use Python Django.

* [Python Django - The Practical Guide](https://www.udemy.com/share/104wQs3@1bRZKG7_5UNHtevDwosC4eWZpqtrUvGa3nxuJJabAWCRZwypeSWaMlcIr1qO-duONw==/)
* [Pagination](https://docs.djangoproject.com/en/4.1/topics/pagination/)

# Change Log
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