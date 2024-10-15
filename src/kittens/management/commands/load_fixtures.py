import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Загружает фикстуры и создает суперпользователя'

    def handle(self, *args, **kwargs):
        breed_fixture_path = os.path.join("kittens", "fixtures", "breeds.json")
        user_fixture_path = os.path.join("kittens", "fixtures", "users.json")
        kitten_fixture_path = os.path.join("kittens", "fixtures", "kittens.json")

        try:
            self.stdout.write(f"Loading breed fixtures from: {breed_fixture_path}")
            call_command("loaddata", breed_fixture_path)
            self.stdout.write(self.style.SUCCESS("Breed fixtures loaded successfully."))

            self.stdout.write(f"Loading users fixtures from {user_fixture_path}")
            call_command("loaddata", user_fixture_path)
            self.stdout.write(self.style.SUCCESS("User fixtures loaded successfully."))

            self.stdout.write(f"Loading kitten fixtures from {kitten_fixture_path }")
            call_command("loaddata", kitten_fixture_path )
            self.stdout.write(self.style.SUCCESS("Kitten fixtures loaded successfully."))

        except Exception as e:
            self.stderr.write(f"Error loading fixtures: {e}")

        
        User = get_user_model()
        username = "admin"
        password = "pass"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
        else:
            self.stdout.write(self.style.WARNING(f'Superusesr "{username}" already exists.'))