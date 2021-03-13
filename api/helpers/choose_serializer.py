from ..serializers import AudiobookSerializer, PodcastSerializer, SongSerializer


def choose_serializer(file_type):
    all_serializers = [AudiobookSerializer, PodcastSerializer, SongSerializer]
    for serializer in all_serializers:
        if serializer.startswith(file_type):
            return serializer
    else:
        return None
