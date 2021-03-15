from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from ..helpers import is_file_type_correct, choose_serializer, get_model
from ..models import Song, Audiobook, Podcast


class GetView(ListAPIView):
    def get(self, request, audioFileType, audioFileID):

        file_type = audioFileType.capitalize()
        model = get_model(file_type)

        file_id = audioFileID

        is_file_type_accepted = is_file_type_correct(file_type)
        serializer_type = choose_serializer(file_type)

        if is_file_type_accepted:
            if file_id is None:
                return Response(
                    {
                        'message': f'{file_type} with id {file_id} was not found',
                        'payload': query.data
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            
            else:
                try:

                    data = model.objects.get(id=file_id)

                    if serializer_type:
                        query = serializer_type(data)
                        return Response(
                            {
                                'message': f'{file_type} with id {file_id} has been successfully found',
                                'payload': query.data
                            }, status=status.HTTP_200_OK
                        )

                    else:
                        return Response(
                            {
                                'message': f'{file_type} with id {file_id} was not found',
                                'payload': query.data
                            }, status=status.HTTP_400_BAD_REQUEST
                        )
                        
                except:
                    return Response(
                            {
                                'message': f'{file_type} with id {file_id} was not found'
                            }, status=status.HTTP_400_BAD_REQUEST
                    )

        else:
            return Response(
                {'message': 'Incorrect audioFileType or audioFileTypeId'}, 
                status=status.HTTP_404_NOT_FOUND
            )
