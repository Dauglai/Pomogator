from api.google_core import create_textfile, set_user_permissions
from api.serializers import TextFileSerializer
from files.models import TextFile
from rest_framework import status, viewsets
from rest_framework.response import Response


class TextFileViewset(viewsets.ModelViewSet):
    queryset = TextFile.objects.all()
    serializer_class = TextFileSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        name = self.serializer_class.validate_name(self.serializer_class, name)
        data = request.data.get('data')
        if name and data:
            doc_id = create_textfile(name, data)
            set_user_permissions(doc_id)
            return super().create(request, *args, **kwargs)
        return Response(self.serializer_class.errors,
                        status=status.HTTP_400_BAD_REQUEST)

