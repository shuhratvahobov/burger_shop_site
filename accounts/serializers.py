from rest_framework import serializers 
from fast_food_app.models import Mahsulotlar
from rest_framework.generics import ListAPIView
from .models import User
class MashulotlarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mahsulotlar
		fields = '__all__'





class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


		def create(self,validated_data):
			auth_user = User.objects.create_user(**validated_data)
			return auth_user








