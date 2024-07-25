from rest_framework import viewsets, permissions, generics, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from django_ratelimit.decorators import ratelimit

from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from .serializers import UserSerializers
#from .permissions import AllowAnyPost



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    #permission_classes = [AllowAnyPost]
    #authentication_classes = (TokenAuthentication)


@method_decorator(ratelimit(key='ip', rate='5/m', method='POST', block=True), name='dispatch')
class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
"""
class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request=request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user is not None:
            login(request, user)
            _, token = AuthToken.objects.create(user)
            return Response({
                'user': {
                    'id': user.id,
                    'username': user.username,
                },
                'token': token
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
"""   

class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (AllowAny,)
