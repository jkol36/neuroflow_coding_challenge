from django.db import models


class Mood(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='moods', null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']