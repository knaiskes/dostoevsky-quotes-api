from django.db import models

class Quote(models.Model):
    text = models.CharField(max_length=120)
    # TODO: add -> book_title

    def __str__(self):
        return self.text
