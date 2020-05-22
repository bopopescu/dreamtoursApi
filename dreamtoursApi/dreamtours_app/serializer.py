from rest_framework import serializers
from dreamtours_app.models import User, City, Particular, Company, LocalType, Local, Rating, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'password',
                  'name',
                  'surname',
                  'email',
                  'birthdate'
        )

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id',
                  'name'
        )

class ParticularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particular
        fields = ('id',
                  'city',
                  'user',
                  'dni',
        )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id',
                  'user',
                  'cif',
                  'phone_number'
        )

class LocalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalType
        fields = ('id',
                  'name'
        )

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ('id',
                  'company',
                  'city',
                  'type',
                  'name',
                  'address'
        )

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id',
                  'particular',
                  'local',
                  'rate'
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',
                  'particular',
                  'local',
                  'comment'
        )