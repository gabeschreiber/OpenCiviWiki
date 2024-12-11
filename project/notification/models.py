"""
Notification model
Notifies users about new followers or replies.
"""
from django.db import models
from accounts.models import Profile
from threads.models import Civi, Thread
from enum import Enum

class ActivityType(Enum):
    NEW_FOLLOWER = "new_follower"
    RESPONSE_TO_CIVI = "response_to_your_civi"
    REBUTTAL_TO_RESPONSE = "rebuttal_to_your_response"


class Notification(models.Model):
    account = models.ForeignKey(
        Profile, null=True, on_delete=models.PROTECT,
        help_text="The profile receiving the notification."
    )
    thread = models.ForeignKey(
        Thread, null=True, on_delete=models.PROTECT,
        help_text="The thread related to the notification."
    )
    civi = models.ForeignKey(
        Civi, null=True, on_delete=models.PROTECT,
        help_text="The Civi solution associated with the notification, if any."
    )

    activity_CHOICES = [(tag.value, tag.name.replace("_", " ").capitalize()) for tag in ActivityType]
    activity_type = models.CharField(
        max_length=31, default=ActivityType.NEW_FOLLOWER.value, choices=activity_CHOICES
    )
    read = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Notification({self.account}, {self.activity_type})"
