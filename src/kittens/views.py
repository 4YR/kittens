from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from kittens.models import Breed, Kitten, Rating
from kittens.serializer import BreedSerializer, KittenDetailSerializer, KittenSerializer
from .permissions import IsOwner


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return KittenDetailSerializer
        return KittenSerializer

    def get_queryset(self):
        queryset = Kitten.objects.all()
        breed_id = self.request.query_params.get("breed_id")
        if breed_id:
            queryset = queryset.filter(breed_id=breed_id)
        return queryset

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

    def perform_update(self, serializer):
        super().perform_update(serializer)

    @action(detail=True, methods=["post"])
    def rate(self, request, pk=None):
        kitten = self.get_object()

        score = request.data.get("score")
        if score is None:
            return Response({"detail": "Требуется оценка."}, status=400)

        rating = Rating.objects.filter(kitten=kitten, user=request.user).first()
        if rating:
            rating.score = request.data["score"]
            rating.save()
        else:
            Rating.objects.create(
                kitten=kitten, user=request.user, score=request.data["score"]
            )
        return Response({"status": "rating set"})
