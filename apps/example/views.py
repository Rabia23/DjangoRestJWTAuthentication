from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.authentication.authentication import UserAuthentication
from apps.authentication.permission import UserAccessPermission


class IndexView(APIView):

    authentication_classes = (UserAuthentication,)
    permission_classes = (UserAccessPermission,)

    def get(self, request):
        data = {
            'message': 'Welcome {} {}'.format(request.user.first_name, request.user.last_name)
        }
        return Response(data, status=status.HTTP_200_OK)
