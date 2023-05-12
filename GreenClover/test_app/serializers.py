from rest_framework import serializers
from test_app.models import Snippet, Info

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    
class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id','dates', 'is_free', 'km']
    
    def create(self, validated_data):
        return Info.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.dates = validated_data.get('dates', instance.dates)
        instance.is_free = validated_data.get('is_free', instance.is_free)
        instance.km = validated_data.get('km', instance.km)
        instance.save()
        return instance