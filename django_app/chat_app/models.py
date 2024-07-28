from django.db import models

class Chat(models.Model):
    user_msg = models.TextField()
    bot_msg = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
