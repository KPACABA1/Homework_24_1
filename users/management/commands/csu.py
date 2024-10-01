from django.core.management import BaseCommand

from users.models import User

# Импортирую данные для почты админа и пароль
from dotenv import load_dotenv
import os
load_dotenv()

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email=os.getenv('mail'))
        user.set_password(os.getenv('password_database'))
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()