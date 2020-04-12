from bson import ObjectId
from rest_framework.response import Response
from rest_framework.views import APIView
import pymongo


class OperaView(APIView):
    server = '39.99.214.102'
    mongo_password = 'Aa12345.'
    mongo = f'mongodb://root:{mongo_password}@{server}:27017/'
    conn = pymongo.MongoClient(mongo)
    db = conn['restapi']

    def get(self, request, id):
        if url := self.db['url'].find_one({'_id': ObjectId(id)}):
            url['_id'] = str(url['_id'])
            return Response({'code': 200, 'msg': 'Query was successful!', 'data': url})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def put(self, request, id):
        data = request.data
        data.pop('_id')
        self.db['url'].update_one({'_id': ObjectId(id)}, {'$set': data})
        return Response({'code': 200, 'msg': 'Opera Successfully!', 'data': None})
