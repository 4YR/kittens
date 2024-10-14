from rest_framework import serializers

from src.kittens.models import Breed, Kitten, Rating


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ["id", "name", "description"]


class KittenSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Kitten
        fields = ["id", "name", "breed", "color", "age_months", "description", "owner"]


class KittenDetailSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    ratings = serializers.StringRelatedField(many=True)

    class Meta:
        model = Kitten
        fields = [
            "id",
            "name",
            "breed",
            "color",
            "age_months",
            "description",
            "owner",
            "ratings",
        ]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "kitten", "user", "score"]
