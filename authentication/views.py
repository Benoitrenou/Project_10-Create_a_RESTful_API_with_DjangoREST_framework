from rest_framework.generics import CreateAPIView
from authentication.serializers import UserSerializer,\
    MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    """
    View to obtain token via JWT
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class SignupView(CreateAPIView):
    """
    View to register user
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
