from Books.models import User, Genre, Stock, Book, Purchase
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from Books.serializers import UserSerializer, GenreSerializer, StockSerializer
from Books.serializers import BookSerializer, PurchaseSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return User.objects.filter(name=username)


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]


class PurchaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
