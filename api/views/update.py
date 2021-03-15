from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from ..helpers import is_file_type_correct, choose_serializer, get_model
from ..models import Song, Audiobook, Podcast


class UpdateView(UpdateAPIView):
    def put(self, request, audioFileType, audioFileID):
        file_type = audioFileType.capitalize()
        file_id = audioFileID

        is_file_type_accepted = is_file_type_correct(file_type)
        serializer_type = choose_serializer(file_type)
        model = get_model(file_type)

        if is_file_type_accepted:

            try: 
                audio_file_instance = model.objects.get(id=file_id)

                serialized_data = serializer_type(audio_file_instance, data=request.data)
                    
                if serialized_data.is_valid():
                    serialized_data.save()
                    return Response(
                        {
                            'message': f'The {file_type} with id {file_id} has been successfully updated',
                            'payload': request.data
                        }, status=status.HTTP_200_OK
                    )
                
                else:
                    return Response(
                        {
                            'message': serialized_data.errors
                        }, status=status.HTTP_400_BAD_REQUEST
                    )

            except:
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
