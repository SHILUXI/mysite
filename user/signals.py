from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from django.contrib.auth.models import User
from django.urls import reverse


@receiver(post_save,sender=User)
def send_notification(sender,instance,**kwargs):
    if kwargs['created'] == True:
        verb = '注册成功'
        url = reverse('user_info')
        notify.send(instance, recipient=instance, verb=verb, action_object=instance, url=url)