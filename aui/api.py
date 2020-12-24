from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .custompermissions import MyPermissions, MyObjPermissions

class UserList(APIView):
    permission_classes = [MyPermissions]
    def get(self, request):
        model = Users.objects.all()
        serializer = UsersSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    permission_classes = [MyObjPermissions, MyPermissions]
    def get_user(self, user_id):
        try:
            model = Users.objects.get(user_id=user_id)
            return model
        except Users.DoesNotExist:
            return

    def get(self, request, user_id):
        if not self.get_user(user_id):
            return Response(f'User with {user_id} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = UsersSerializer(self.get_user(user_id))
        return Response(serializer.data)

    def put(self, request, user_id):
        serializer = UsersSerializer(self.get_user(user_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        if not self.get_user(user_id):
            return Response(f'User with {user_id} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(user_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)