from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Mood(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='moods', null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=250, null=True)
    streak = models.IntegerField(null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()