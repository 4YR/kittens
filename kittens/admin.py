from django.contrib import admin

from kittens.models import Breed, Kitten, Rating


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    list_display = ["name", "breed", "color", "age_months", "owner"]
    search_fields = ["name", "breed__name", "color"]
    list_filter = ["breed", "age_months"]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["kitten", "user", "score"]
    list_filter = ["score"]
