from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextFileSerializer
from .models import File
from .utils import create_google_doc
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

file_types = {
    "document": "application/vnd.google-apps.document",
    "presentation": "application/vnd.google-apps.presentation",
    "sheet": "application/vnd.google-apps.spreadsheet",
    "folder": "application/vnd.google-apps.folder",
    "photo": "application/vnd.google-apps.photo"
}

class CreateGoogleDocView(APIView):

    def get(self, request):
        txt = File.objects.all()
        return Response({'posts': TextFileSerializer(txt, many=True).data})

    def post(self, request):
        serializer = TextFileSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            data = serializer.validated_data['data']
            id = serializer.validated_data['event_id']
            type = serializer.validated_data['type']
            try:
                document_id = create_google_doc(name, data, type, id )
                return Response({"message": "Документ успешно создан.", 'link': f'https://docs.google.com/document/d/{document_id}'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)