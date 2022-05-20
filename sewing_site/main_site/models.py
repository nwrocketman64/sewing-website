from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image

# Create your models here.


class Project(models.Model):
    """ Project
    The class is a model for how the projects are stored in a database.
    """
    title = models.CharField(max_length=50)
    description = models.TextField()
    external_url = models.URLField(max_length=200, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True, editable=False)
    slug = models.SlugField(default="", blank=True, editable=False,
                            null=False, db_index=True, unique=True)
    image = models.ImageField(upload_to="images")


    # The function defines how each project appears in admin.
    def __str__(self):
        return f"{self.title} - Last Updated: {self.last_update.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function creates the slug and sets the last update.
    def save(self, *args, **kwargs):
        # Create the slug for the entry.
        self.slug = slugify(self.title)

        # Create datetime object and set it to now.
        current_time = datetime.now()

        # Set sent time to the current time.
        self.last_update = current_time

        # Save everything else.
        super().save(*args, **kwargs)


class Request(models.Model):
    """ Request
    The class defines how request from the contact form are saved.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    comment = models.TextField()
    sent_time = models.DateTimeField(editable=False)


    # The function defines how each request appears in admin.
    def __str__(self):
        return f"{self.first_name} {self.last_name} on {self.sent_time.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function saves sent_time as the current time the request was
    # saved.
    def save(self, *args, **kwargs):
        # Create datetime object and set it to now.
        current_time = datetime.now()

        # Set sent time to the current time.
        self.sent_time = current_time

        # Save everything else.
        super().save(*args, **kwargs)
