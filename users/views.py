from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserInfoSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userinfo(request):
    item = CustomUser.objects.all()
    serializer = UserInfoSerializer(item, many=False)
    return Response(serializer.data)
