from unittest.util import _MAX_LENGTH
from django.db import models

# This class allows you to define how an entity is defined in the database
class drey_link_saved(models.Model):
    # For example, here we will have a url corresponding to the long link and the idd corresponding to our character sequence
    url = models.CharField(max_length=10000)
    idd = models.CharField(max_length=10)

    # The following lines allow you to modify the name under which each entity will be saved in the database
    # I just added my nickname in front of the link
    def __str__(self):
        return "Drey : " + self.url