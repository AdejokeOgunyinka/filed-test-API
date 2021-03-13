from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from ..helpers import is_file_type_correct, choose_serializer
from ..models import Song, Audiobook, Podcast


class DeleteView(DestroyAPIView):
    def delete(self, request):
        file_type = str(request.META.get('audioFileType', None)).capitalize()
        file_id = request.META.get('audioFileId', None)

        is_file_type_accepted = is_file_type_correct(file_type)
        serializer_type = choose_serializer(file_type)

        if is_file_type_accepted:
            audio_file_instance = file_type.objects.get(id=file_id)

            if audio_file_instance:
                audio_file_instance.delete()
                return Response(
                    {
                        'message': f'This {file_type} with id {file_id} has been successfully deleted'
                    }, status=status.HTTP_200_OK
                )

            else:
                return Response(
                    {
                        'message': f'This {file_type} with id {file_id} does not exist'
                    }, status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                {
                    'message': 'Please ensure you entered the correct file type'
                }, status=status.HTTP_400_BAD_REQUEST
            )
