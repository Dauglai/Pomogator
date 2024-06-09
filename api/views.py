from django.shortcuts import get_object_or_404
from googleapiclient.discovery import build
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateFileSerializer, FileSerializer
from .models import File
from .utils import create_google_file, get_credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

file_types = {
    "document": "https://docs.google.com/document/d/",
    "presentation": "https://docs.google.com/presentation/d/",
    "sheet": "https://docs.google.com/spreadsheets/d/",
    "folder": "application/vnd.google-apps.folder",
    "photo": "application/vnd.google-apps.photo",
    "forms": "https://docs.google.com/forms/d/"
}

class GoogleFilesView(APIView):

    def get(self, request):
        txt = File.objects.all()
        return Response(FileSerializer(txt, many=True).data)

    @swagger_auto_schema(request_body=CreateFileSerializer)
    def post(self, request):
        serializer = CreateFileSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            data = serializer.validated_data['data']
            id = serializer.validated_data['event_id']
            type = serializer.validated_data['type']
            if type == "":
                return Response({"error": f"Указан неправильный тип документа"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            fileId = create_google_file(name, data, type, id)
            return Response({'message': 'Документ успешно создан.', 'link': f'{file_types[type]}{fileId}'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleFilesDetail(APIView):
    def get(self, request, pk):
        file = get_object_or_404(File, pk=pk)
        serializer = FileSerializer(file)
        return Response(serializer.data)


    def delete(self, request, pk):
        file = get_object_or_404(File, pk=pk)
        service = build('drive', 'v3', credentials=get_credentials())
        service.files().delete(fileId=file.file_id).execute()
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)