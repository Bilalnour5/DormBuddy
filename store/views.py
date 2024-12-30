from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.exceptions import PermissionDenied
from .models import Properties, Cart
from .serializers import PropertiesSerializer , CartSerializer
from .pagination import DefaultPagination
from .filters import PropertyFilter
# Create your views here

class PropertyViewSet(ModelViewSet):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ['title', 'city', 'descriptiontranslated']
    ordering_fields = ['rent', 'title']

    def get_permissions(self):
        # Allow read-only access to everyone
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        # Require admin privileges for write actions
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        # Ensure only admins can create
        if not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to create properties.")
        serializer.save()

    def perform_destroy(self, instance):
        # Ensure only admins can delete
        if not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to delete properties.")
        instance.delete()


class UserCartView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

    def get(self, request, *args, **kwargs):
        # Fetch the wishlist for the authenticated user
        try:
            cart = Cart.objects.get(user=request.user)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=200)
        except cart.DoesNotExist:
            return Response({"detail": "Wishlist not found."}, status=404)
         
