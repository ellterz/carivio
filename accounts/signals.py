
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile


@receiver(post_save, sender=Profile)
def profile_created(sender, instance, created, **kwargs):
    if created:
        from accounts.tasks import send_welcome_email
        from django.contrib.auth.models import Group
        send_welcome_email.delay(instance.pk)
        garage_owner_group, _ = Group.objects.get_or_create(name='Garage Owner')
        instance.groups.add(garage_owner_group)