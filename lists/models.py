from django.db import models
from utils.models import Timestamps
from django.contrib.auth import get_user_model

class List(Timestamps):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True) 

    def __str__(self):
        return self.name


class ListItem(Timestamps):
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text