from rest_framework import views, response, authentication
from .serializers import UserRegisterSerializer, UserLoginSerializer



# Register view
class UserRegisterView(views.APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)



# Login view
class UserLoginView(views.APIView):
    authentication_classes = [authentication.SessionAuthentication, authentication.BasicAuthentication]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data)