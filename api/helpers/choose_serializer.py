from ..serializers import AudiobookSerializer, PodcastSerializer, SongSerializer


def choose_serializer(file_type):
    string_serializers = ['AudiobookSerializer', 'PodcastSerializer', 'SongSerializer']
    all_serializers = [AudiobookSerializer, PodcastSerializer, SongSerializer]

    for serializer in string_serializers:
        if serializer.startswith(file_type):
            # print(serializer)
            for real_serializer in all_serializers:
                if serializer == str(real_serializer):
                    # print(real_serializer)
                    return real_serializer
        else:
            return None
