import os
from django.core.management import call_command
from django.contrib.auth import get_user_model


def run():

    user_fixture_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "users.json"
    )
    kitten_fixture_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "kittens.json"
    )

    try:

        print(f"Loading user fixtures from: {user_fixture_path}")
        call_command("loaddata", user_fixture_path)
        print("User fixtures loaded successfully.")

        print(f"Loading kitten fixtures from: {kitten_fixture_path}")
        call_command("loaddata", kitten_fixture_path)
        print("Kitten fixtures loaded successfully.")
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
