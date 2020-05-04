from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# A Serializer basically packages up and sends data to and from the API in a format each tech can understand. 

class SnippetSerializer(serializers.ModelSerializer):
    #  Here we name the serializer class, and extend it off the ModelSerializer class.
    #  You can just have your own general serialize, but a Model one is a conscise and neat way
    #  To write your serialiser if you don't need much personalisation. 
    class Meta:
        model = Snippet
        #  These are the fields that get serialised.
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

