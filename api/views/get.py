from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from ..helpers import is_file_type_correct, choose_serializer
from ..models import Song, Audiobook, Podcast


class GetView(ListAPIView):
    def get(self, request):
        file_type = str(request.META.get('audioFileType', None)).capitalize()
        file_id = request.META.get('audioFileId', None)

        is_file_type_accepted = is_file_type_correct(file_type)
        serializer_type = choose_serializer(file_type)

        if is_file_type_accepted:
            if file_id is None:
                data = str(file_type).objects.all()
            
            else:
                data = str(file_type).objects.get(id=file_id)

        if data:
            if serializer_type:
                query = serializer_type(data=data)

            else:
                return Response(
                    {
                        'message': f'{file_type} has been successfully found',
                        'payload': query.data
                    }, status=status.HTTP_200_OK
                )
        else:
            return Response(
                    {'message': 'Incorrect audioFileType or audioFileTypeId'}, 
                    status=status.HTTP_404_NOT_FOUND
                )
