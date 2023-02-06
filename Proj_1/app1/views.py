from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView

# py manage.py migrate for operational error

@api_view(http_method_names=['POST','GET','PUT','PATCH','DELETE'])
def first_api(request):
    params = request.query_params
    print(params)
    if request.method == 'POST':
        data = request.data
        if data:
            return Response(data=data)
        data = {'detial': 'Enter some data before sending requests.'}
        return Response(data=data)

    if request.method == 'PUT':
        data = request.data
        if data:
            return Response(data=data)
        data = {"detail": "Enter some data before sending requests."}
        return Response(data=data)
    data = {"detail": "This API is created for demo."}
    return Response(data=data)

class Second_api(APIView):

    def get(self, request):
        return Response(data={'detail': 'This is class based API'})

    def post(self, request):
        data = request.data
        return Response(data=data)
    
    def put(self, request):
        data = request.data
        return Response(data=data)
    
    def delete(self, request):
        return Response(data={'detail': "This is delete request"})