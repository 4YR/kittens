from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from src.kittens.models import Breed, Kitten, Rating
from kittens.serializer import BreedSerializer, KittenDetailSerializer, KittenSerializer


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated]

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
        if instance.owner != self.request.user:
            raise PermissionDenied("Вы можете удалить только своих собственных котят.")
        instance.delete()

    def perform_update(self, serializer):
        if serializer.instance.owner != self.request.user:
            raise PermissionDenied(
                "Вы можете редактировать только своих собственных котят."
            )
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
