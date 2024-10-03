from django.db import models
from django.contrib.auth.models import User


class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Kitten(models.Model):
    name = models.CharField(max_length=100)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="kittens")
    color = models.CharField(max_length=100)
    age_months = models.PositiveIntegerField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kittens")

    def __str__(self):
        return self.name


class Rating(models.Model):
    kitten = models.ForeignKey(Kitten, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    class Meta:
        unique_together = ("kitten", "user")
