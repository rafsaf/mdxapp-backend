from typing import List, Tuple
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    CHARACTERS: List[Tuple[str, str]] = [
        ("writer", "Writer"),
        ("dev", "Developer"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    character = models.CharField(choices=CHARACTERS, max_length=10)
