from rest_framework import serializers
from .models import Actor,Movie,Review

###########get all list ##########################

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Actor
        fields = ('id','name')

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title','overview',)

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)

###########movie detail######################

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)

class ActorNameSerializer(serializers.ModelSerializer):

    class Meta:

        model = Actor
        fields = ('name',)

class MovieDetailSerializer(serializers.ModelSerializer):

    actors = ActorNameSerializer(many=True,read_only=True)

    review_set = ReviewSerializer(many=True,read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

###########actor detail###############################
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class ActorSerializer(serializers.ModelSerializer):

    movies = MovieSerializer(many=True,read_only=True)

    class Meta:

        model = Actor
        fields = ('id','movies','name',)

###############review detial ########################

class ReviewDetailSerializer(serializers.ModelSerializer):
    
    ##many=True인가 many=True가 아닌가..?
    ##review 하나에 영화가 여러개일수는 없다
    ##primarykeyrelatedfield는 id를 가지고있는
    movie = MovieSerializer(read_only=True)

    class Meta:

        model = Review
        fields = ('id','movie','title','content',)
