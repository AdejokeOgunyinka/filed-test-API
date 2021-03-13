from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from ..helpers import is_file_type_correct, choose_serializer
from ..models import Song, Audiobook, Podcast


class CreateView(CreateAPIView):
    def post(self, request):
        file_type = str(request.META.get('audioFileType', None)).capitalize()
        file_id = request.META.get('audioFileId', None)

        is_file_type_accepted = is_file_type_correct(file_type)
        serializer_type = choose_serializer(file_type)

        if is_file_type_accepted:
            serialized_data = serializer_type(data=request.data)

            if serialized_data.is_valid():
                serialized_data.save()
                return Response(
                    {
                        'message': f' New {file_type} has been successfully saved',
                        'payload': request.data
                    }, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                        'message': 'Please make sure that the information you entered is correct'
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                    {
                        'message': 'Please make sure you enter the correct file type'
                    }, status=status.HTTP_400_BAD_REQUEST
            )
