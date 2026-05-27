from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crea el usuario administrador inicial'

    def handle(self, *args, **kwargs):
        username = 'egibide'
        password = '12345Abcde'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'El usuario "{username}" ya existe.'))
            return

        User.objects.create_superuser(username=username, password=password, email='')
        self.stdout.write(self.style.SUCCESS(f'Usuario "{username}" creado correctamente.'))
