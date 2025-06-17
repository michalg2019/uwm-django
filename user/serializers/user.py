from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User
from event.models import UserProfile


class ShortUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'username', 'email')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
		data['user'] = UserSerializer(self.user).data
		return data

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('id', 'user', 'bio', 'birth_date', 'phone_number',
		          'profile_picture', 'interests', 'created_at', 'updated_at')
		read_only_fields = ('created_at', 'updated_at')

class UserSerializer(serializers.ModelSerializer):
	profile = UserProfileSerializer(required=False)


	class Meta:
		model = User
		exclude = ('password',)


	def create(self, validated_data):
		profile_data = validated_data.pop('profile', {})
		user = User.objects.create(**validated_data)
		UserProfile.objects.create(user=user, **profile_data)
		return user


	def update(self, instance, validated_data):
		profile_data = validated_data.pop('profile', {})
		if profile_data:
			profile = instance.profile
			for attr, value in profile_data.items():
				setattr(profile, attr, value)
			profile.save()
		return super().update(instance, validated_data)
