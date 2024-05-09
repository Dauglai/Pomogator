from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextFileSerializer
from .models import File
from .utils import create_google_doc, create_google_sheet, create_google_pres, create_google_forms
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

file_types = {
    "document": "https://docs.google.com/document/d/",
    "presentation": "https://docs.google.com/presentation/d/",
    "sheet": "https://docs.google.com/spreadsheets/d/",
    "folder": "application/vnd.google-apps.folder",
    "photo": "application/vnd.google-apps.photo",
    "forms": "https://docs.google.com/forms/d/"
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
                fileId = ""
                if type == "document":
                    fileId = create_google_doc(data, name, id)
                if type == "sheet":
                    fileId = create_google_sheet(data, name, id)
                if type == "presentation":
                    fileId = create_google_pres(data, name, id)
                if type == "forms":
                    fileId = create_google_forms(data, name, id)
                if type == "":
                    return Response({"error": f"Указан неправильный тип документа"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                return Response({'message': 'Документ успешно создан.', 'link': f'{file_types[type]}{fileId}'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)