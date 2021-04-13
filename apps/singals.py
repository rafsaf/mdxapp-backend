from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.models import App


@receiver(post_save, sender=App)
def update_app_after_save(sender, instance: App, created: bool, **kwargs) -> None:
    if created:
        instance.users.add(instance.owner)
        instance.save()
    people: int = instance.users.count()
    if instance.people != people:
        instance.people = people
        instance.save()
