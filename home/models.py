from django.db import models
from .choices import choice,plusOnes
from django.contrib.auth.models import User
from django.utils import timezone

class UserFullName(User):
    class Meta:
        proxy=True
        verbose_name= 'Guest RSVP'
        verbose_name_plural = 'Guests RSVPs'

    def __str__(self):
        return self.get_full_name()

class RSVP(models.Model):
    user = models.ForeignKey(UserFullName, on_delete=models.CASCADE)
    reception = models.CharField(max_length=20,choices=choice,default='No Response')
    extra = models.CharField(max_length=10,choices=plusOnes,default=0)  

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Post(models.Model):
    user = models.ForeignKey(UserFullName, on_delete='cascade')
    post = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post
