from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.users.serializers import UserSerializer
from app.models import AuthUser


class UserViews(generics.ListAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.query_params.get('status'):
            queryset = AuthUser.objects.filter(is_active = self.request.query_params.get("status")).order_by('-id')
            return queryset
        else:
            queryset = AuthUser.objects.all()
            return queryset