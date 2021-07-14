from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notes(models.Model):
    # class representing Notes database
    notes_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)

    @property
    def is_notes_instance(self):
        """
        method used specifically for testing purpose
        :return:
        """
        return self.id > 0
