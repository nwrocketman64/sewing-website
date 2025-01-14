from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from PIL import Image as PILImage, ImageOps
import pytz

# Create your models here.


class Image(models.Model):
    """Images
    The class is a model for how the images of the projects are stored.
    """
    image_title = models.CharField(max_length=50)
    date_created = models.DateTimeField(blank=True, null=True, editable=False)
    image = models.ImageField(upload_to="images")
    # priority = models.PositiveIntegerField(blank=False, default=1, null=False)

    # The function defines how each image appears in admin.
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        timezone_time = self.date_created.now(pytz.timezone(settings.TIME_ZONE))

        # Return the string of the object.
        return f"{self.image_title} - Uploaded on: {timezone_time.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function creates the slug and sets the last update.
    def save(self, *args, **kwargs):
        # Set sent time to the current time.
        self.date_created = datetime.now()

        # Save everything else.
        super().save(*args, **kwargs)

        # Set the base width and height for the thumbnail of the image.
        base_width = 700
        base_height = 700

        # Grab the image that was just saved.
        img_data = PILImage.open(self.image.path)

        # Use exif_transpose to maintain image EXIF metadata.
        img = ImageOps.exif_transpose(img_data)

        # Resize the image that was just save and then save the image.
        img.thumbnail((base_width, base_height), PILImage.LANCZOS)
        img.save(self.image.path)


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
    images = models.ManyToManyField(Image)


    # The function defines how each project appears in admin.
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        timezone_time = self.last_update.now(pytz.timezone(settings.TIME_ZONE))

        # Return the string of the object.
        return f"{self.title} - Last Updated: {timezone_time.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function creates the slug and sets the last update.
    def save(self, *args, **kwargs):
        # Create the slug for the entry.
        self.slug = slugify(self.title)

        # Set sent time to the current time.
        self.last_update = datetime.now()

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
        # Convert from UTC time to the proper timezone.
        timezone_time = self.sent_time.now(pytz.timezone(settings.TIME_ZONE))

        # Return the string of the object.
        return f"{self.first_name} {self.last_name} on {timezone_time.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function saves sent_time as the current time the request was
    # saved.
    def save(self, *args, **kwargs):
        # Set sent time to the current time.
        self.sent_time = datetime.now()

        # Save everything else.
        super().save(*args, **kwargs)
