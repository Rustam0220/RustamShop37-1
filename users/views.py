from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        profile_serializer = UserProfileSerializer(data={})

        if user_serializer.is_valid():
            user = user_serializer.save()
            profile = UserProfile.objects.create(user=user)
            profile.activation_code = profile.generate_activation_code()
            profile.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

@api_view(['POST'])
def confirm_user(request):
    if request.method == 'POST':
        activation_code = request.data.get('activation_code')
        try:
            profile = UserProfile.objects.get(activation_code=activation_code)
            user = profile.user
            user.is_active = True
            user.save()
            return Response({'message': 'User confirmed successfully.'})
        except UserProfile.DoesNotExist:
            return Response({'message': 'Invalid activation code.'}, status=status.HTTP_400_BAD_REQUEST)