from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextFileSerializer
from .models import GoogleDoc
from .utils import create_google_doc
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class CreateGoogleDocView(APIView):

    def get(self, request):
        txt = GoogleDoc.objects.all()
        return Response({'posts': TextFileSerializer(txt, many=True).data})

    def post(self, request):
        serializer = TextFileSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            data = serializer.validated_data['data']
            try:

                document_id = create_google_doc(name, data)
                return Response({"message": "Документ успешно создан.", 'link': f'https://docs.google.com/document/d/{document_id}/'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)