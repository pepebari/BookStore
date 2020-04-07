from rest_framework import viewsets
from rest_framework import permissions

from Books.models import User, Genre, Stock, Book, Purchase
from Books.serializers import UserSerializer, GenreSerializer, StockSerializer
from Books.serializers import BookSerializer, PurchaseSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to view or edit Users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super(UserViewSet, self).get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name=name)
        return qs


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to view or edit Genres.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super(GenreViewSet, self).get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name=name)
        return qs


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to view or edit Stocks.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super(StockViewSet, self).get_queryset()
        quantity = self.request.query_params.get('quantity')
        if quantity:
            qs = qs.filter(quantity=quantity)
        return qs


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to view or edit Books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super(BookViewSet, self).get_queryset()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        if title:
            qs = qs.filter(title=title)
        if author:
            qs = qs.filter(author=author)
        return qs


class PurchaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to view or edit Purchases.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super(PurchaseViewSet, self).get_queryset()
        userId = self.request.query_params.get('userId')
        bookId = self.request.query_params.get('bookId')
        if userId:
            qs = qs.filter(user__id=userId)
        if bookId:
            qs = qs.filter(book__id=bookId)
        return qs
