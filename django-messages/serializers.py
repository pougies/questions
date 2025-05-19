from rest_framework import serializers

from . import models as message_models

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message_models.Message
        fields = (
            "id",
            "thread",
            "body",
            "author",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class MessageThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = message_models.MessageThread
        fields = [
            "id",
            "title",
            "created_at",
            "created_by",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "created_by",
        ]


class DetailedMessageThreadSerializer(MessageThreadSerializer):
    message_list = MessageSerializer(many=True)

    class Meta:
        model = message_models.MessageThread
        fields = MessageThreadSerializer.Meta.fields + [
            "message_list",
        ]

        read_only_fields = MessageThreadSerializer.Meta.read_only_fields + [
            "message_list",
        ]