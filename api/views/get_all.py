from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from ..helpers import is_file_type_correct, choose_serializer, get_model
from ..models import Song, Audiobook, Podcast


class GetAllView(ListAPIView):
    def get(self, request, audioFileType):

        file_type = audioFileType.capitalize()
        model = get_model(file_type)


        is_file_type_accepted = is_file_type_correct(file_type)
        serializer_type = choose_serializer(file_type)

        if is_file_type_accepted:

            try:
                data = model.objects.all()

                if serializer_type:
                    query = serializer_type(data, many=True)
                    return Response(
                        {
                            'message': f'{file_type}(s) have been successfully found',
                            'payload': query.data
                        }, status=status.HTTP_200_OK
                    )

                else:
                    return Response(
                        {
                            'message': f'{file_type}(s) were not found',
                            'payload': query.data
                        }, status=status.HTTP_400_BAD_REQUEST
                    )
            except:
                return Response(
                    {
                        'message': f'No {file_type} was found',
                        'payload': query.data
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                    {'message': 'Incorrect audioFileType or audioFileTypeId'}, 
                    status=status.HTTP_400_BAD_REQUEST
            )
