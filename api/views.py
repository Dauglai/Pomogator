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
            gauth = GoogleAuth()
            gauth.LocalWebserverAuth()
            drive = GoogleDrive(gauth)
            try:

                doc_file = drive.CreateFile({'title': f'{name}'})
                doc_file.SetContentString(data)
                doc_file.Upload()
                #document_id = create_google_doc(data, name)
                document_id = doc_file.get('id')
                return Response({'message': 'Документ успешно создан.', 'link': f'https://docs.google.com/document/d/{document_id}'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)