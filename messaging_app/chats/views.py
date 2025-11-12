from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Conversation, Message
from .serializers import ConversationSerializer,MessageSerializer
# Create your views here.

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing, creating, and retrieving conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and creating messages
    """
    queryset = Message.objects.all()
    serializer_class = ConversationSerializer
