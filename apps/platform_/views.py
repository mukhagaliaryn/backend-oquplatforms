from rest_framework import views, status, permissions
from rest_framework.response import Response


class MainAPIView(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request):
        data = {
            'message': 'Hello Django!'
        }
        return Response(data, status=status.HTTP_200_OK)
