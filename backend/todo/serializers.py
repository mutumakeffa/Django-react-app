# We need serializers to convert model instances to JSON so that the frontend can work with the received data easily. 

from rest_framework import serializers
from .models import Todo


# we specify the model to work with and the fields we want to be converted to JSON.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
