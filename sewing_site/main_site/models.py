from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


# class Projects(models.Model):
    # title = models.CharField(max_length=50)
    # description = models.TextField()
    # external_url = models.URLField(max_length=200)


class Request(models.Model):
    """ Request
    The class defines how request from the contact form are saved.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    comment = models.TextField()
    sent_time = models.DateTimeField()

    # The function defines how each request appears in admin.
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.sent_time}"

    # The function saves sent_time as the current time the request was
    # saved.
    def save(self, *args, **kwargs):
        # Create datetime object and set it to now.
        current_time = datetime.now()

        # Set sent time to the current time.
        self.sent_time = current_time

        # Save everything else.
        super().save(*args, **kwargs)
