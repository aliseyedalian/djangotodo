from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:  # for showing items' names in admin section
        return self.item + ', ' + str(self.completed)