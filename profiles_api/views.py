from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
  """Test API View"""

  def get(self, request ,format=None):
    """Returns a list of APIView features"""
    an_apiview = [
      'Uses HTTP methods as functions (get, post, patch, put, delete)',
      'Is similar to a traditinak Django View',
      'Gives you the most control over you application logic',
      'Is mapped manully to URLs',
    ]

    return Response({ 'message': 'hello!', 'an_apiview': an_apiview })