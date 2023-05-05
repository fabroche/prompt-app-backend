from rest_framework import serializers
from promptApp.models.prompt.prompt import Prompt


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = '__all__'
