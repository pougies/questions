from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser

class MessageThread(models.Model):
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(AbstractBaseUser, on_delete=models.CASCADE)

    @property
    def message_list(self):
        return self.messages.all()


class Message(models.Model):
    author = models.ForeignKey(AbstractBaseUser, on_delete=models.CASCADE)

    body = models.TextField(default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    thread = models.ForeignKey(on_delete=models.CASCADE, related_name="messages")