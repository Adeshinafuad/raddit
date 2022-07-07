from rest_framework import serializers
from .models import Post,Vote

class PostSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    author_id = serializers.ReadOnlyField(source="author.id")
    votes = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        # fields = ['id','title', 'url', 'text', 'created']
        fields = '__all__'
        
    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()
            
    
class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']