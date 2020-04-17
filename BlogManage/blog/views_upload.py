from rest_framework.response import Response
from rest_framework.views import APIView


class UploadView(APIView):
    def post(self, request):
        try:
            print(request.FILES)
            return Response(
                {'code': 200, 'msg': 'Upload Successfully!', 'data': 'https://api.ahriknow.com/image?album=girl,1'})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})
