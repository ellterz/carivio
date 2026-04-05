from celery import shared_task
from django.contrib.auth import get_user_model

Profile = get_user_model()


@shared_task
def send_welcome_email(user_id):
    try:
        user = Profile.objects.get(pk=user_id)
        print(f"Welcome email sent to {user.username} at registration.")
    except Profile.DoesNotExist:
        pass