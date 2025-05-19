from rest_framework.response import Response
from rest_framework import viewsets, mixins, views, permissions

from . import serializers as message_serializers
from . import models as message_models

class MessageAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        message_data = request.data | {
            "author": request.user.id
        }

        message_serializer = message_serializers.MessageSerializer(message_data)
        message_serializer.is_valid(raise_exception=True)
        message_serializer.save()

        return Response(message_serializer.data)


class MessageThreadViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = message_models.MessageThread.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return message_serializers.DetailedMessageThreadSerializer
        return message_serializers.MessageThreadSerializer