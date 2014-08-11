from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from jsonfield import JSONField

import base64
import hashlib
import datetime

class Passage(models.Model):
    user = models.ForeignKey(User, related_name='passages')
    hash_key = models.CharField(max_length=8, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    passage_data = JSONField(blank=True, null=True)
    
    def __unicode__(self):
        if self.passage_data.has_key("name"):
            return self.passage_data["name"]
        else:
            return str(self.date_created)
        
    def get_absolute_url(self):
        return reverse('planner-detail', kwargs={'slug': self.hash_key})

    def save(self, *args, **kwargs):
        """
            Save the field with a unique "hash_key"
        """
        if not self.hash_key:
            hasher = hashlib.sha1("".join([self.user.username,
                                            datetime.datetime.now().isoformat()]))
            self.hash_key = base64.urlsafe_b64encode(hasher.digest())[0:7]
        super(Passage, self).save()

"""
    Signal Handlers
"""
from allauth.account.signals import user_signed_up
from allauth.socialaccount.signals import social_account_added
import stathat

def signup_signal_callback(sender, **kwargs):
    # stathat statistic for new registrations
    stathat.ez_count('ben@bilgecode.com', 'Users Registered', 1)

user_signed_up.connect(signup_signal_callback)
social_account_added.connect(signup_signal_callback)  # most likely a registration