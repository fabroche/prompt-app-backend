from rest_framework import viewsets

from promptApp.models.prompt.prompt import Prompt
from ..serializers.promptSerializer import PromptSerializer


class PromptView(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    queryset = Prompt.objects.all()
