import os
from django.core.management import call_command
from django.contrib.auth import get_user_model


def run():

    try:
        fixture_path = os.path.join(os.path.dirname(__file__), "kittens", "fixtures", "initial_data.json")
        print(f"Loading fixtures from: {fixture_path}")
        call_command("loaddata", fixture_path)
        print("Fixtures loaded successfully.")
    except Exception as e:
        print(f"Error loading fixtures: {e}")

    User = get_user_model()
    username = "admin"
    password = "pass"
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, password=password)
        print(f'Superuser "{username}" created successfully.')
    else:
        print(f'Superuser "{username}" already exists.')


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cats.settings")
    import django

    django.setup()
    run()
