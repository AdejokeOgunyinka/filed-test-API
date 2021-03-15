from ..serializers import AudiobookSerializer, PodcastSerializer, SongSerializer
# from ..import serializers


def choose_serializer(file_type):
    all_serializers = {"AudiobookSerializer": AudiobookSerializer, "PodcastSerializer": PodcastSerializer, "SongSerializer": SongSerializer}

    for serializer in all_serializers.keys():
        if serializer.startswith(file_type):
            return all_serializers[serializer]
