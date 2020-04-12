from bson import ObjectId
from rest_framework.response import Response
from rest_framework.views import APIView
from RestapiManage.restapi.models import Project, Url
from RestapiManage.restapi.serializer import ManyProject, ManyUrl
import pymongo


class UrlView(APIView):
    server = '39.99.214.102'
    mongo_password = 'Aa12345.'
    mongo = f'mongodb://root:{mongo_password}@{server}:27017/'
    conn = pymongo.MongoClient(mongo)
    db = conn['restapi']

    def get(self, request):
        urls = Url.objects.filter(user=request.u)
        data = ManyUrl(instance=urls, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            data = request.data
            if project := Project.objects.filter(pk=data.get('project')).first():
                _id = self.db['url'].save({
                    'auth': project.auth,
                    'url': data.get('url'),
                    'method': data.get('method'),
                    'describe': data.get('describe'),
                    'opera_list': [],
                    'return': {
                        'type': 'string',
                        'data': 'Return Data.'
                    }
                })
                url = Url(path=data.get('url'), method=data.get('method'), describe=data.get('describe'),
                          url_id=_id, user=request.u, project=project)
                url.save()
            return Response({'code': 200, 'msg': 'Opera Successfully!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request):
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if url := Url.objects.filter(pk=id).first():
            self.db['url'].delete_many({'_id': ObjectId(url.url_id)})
            url.delete()
            return Response({'code': 200, 'msg': 'Delete successful!'})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
