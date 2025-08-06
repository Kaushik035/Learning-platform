from django.db import models

class Clickstream(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    event_context = models.CharField(max_length=255)
    component = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    description = models.TextField()
    origin = models.CharField(max_length=20)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.time} - {self.event_name}"
