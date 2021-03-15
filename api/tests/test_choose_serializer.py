from django.test import TestCase
from ..helpers.choose_serializer import choose_serializer
from ..serializers import SongSerializer, PodcastSerializer, AudiobookSerializer


class TestChooseSerializer(TestCase):
    def setUp(self):
        self.exec = lambda file_type: choose_serializer(file_type)

    def test_song_serializer(self):
        file_type = "Song"
        serializer = self.exec(file_type)
        self.assertEqual(serializer, SongSerializer)

    def test_podcast_serializer(self):
        file_type = "Podcast"
        serializer = self.exec(file_type)
        self.assertEqual(serializer, PodcastSerializer)

    def test_audiobook_serializer(self):
        file_type = "Audiobook"
        serializer = self.exec(file_type)
        self.assertEqual(serializer, AudiobookSerializer)
