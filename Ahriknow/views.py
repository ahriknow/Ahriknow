from rest_framework.response import Response
from rest_framework.views import APIView


class IndexView(APIView):
    def get(self, request):
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': None})
