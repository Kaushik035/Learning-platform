from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Clickstream
from .serializers import ClickstreamSerializer

class ClickstreamLogView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['ip_address'] = request.META.get('REMOTE_ADDR')
        if request.user.is_authenticated:
            data['user'] = request.user.id

        serializer = ClickstreamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Clickstream logged"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
