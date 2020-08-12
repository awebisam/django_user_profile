from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''Test API View'''

    def get(self, request, format=None):
        """Returns A list of APIView features"""
        an_apiview = [
            'Uses Http methods as f(get, put, post, patch and delete)',
            'Similar to a Django CBV',
            'Gives more control',
            'Mapped Manually',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
