from secrets import token_urlsafe
from django.db import models
from django.contrib.auth.models import User


class App(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=300, default="", unique=True, blank=True)
    users = models.ManyToManyField(User, related_name="users", blank=True)
    people = models.PositiveIntegerField(default=1, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.token == "":
            self.token = token_urlsafe(50)
        super(App, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
