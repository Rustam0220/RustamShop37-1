from django.db import models
from django.contrib.auth.models import User
import random
import string

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=6, blank=True)

    def generate_activation_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))