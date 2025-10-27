# library/views.py
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

class BookSearchView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        q = request.query_params.get('q', '')
        if not q:
            return Response({"error": "Укажите параметр 'q'"}, status=400)
        books = Book.objects.filter(
            Q(title__icontains=q) |
            Q(genre__icontains=q) |
            Q(author__first_name__icontains=q) |
            Q(author__last_name__icontains=q)
        ).distinct()
        return Response(BookSerializer(books, many=True).data)