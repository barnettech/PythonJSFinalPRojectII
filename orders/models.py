from django.db import models

# Model to hold all the food items for the menu.
class Highscore(models.Model):
    """
    Model representing a food on the menu (but not a specific copy of a food).
    """
    besttime = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.username