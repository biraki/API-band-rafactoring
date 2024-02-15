from .models import Album
from .serializers import AlbumSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AlbumView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        for attr_name in dir(self):
              if not callable(getattr(self, attr_name)) and not attr_name.startswith("__"):
                   print(f"{attr_name}: {getattr(self, attr_name)}","*****************")

        serializer.save(user=self.request.user)