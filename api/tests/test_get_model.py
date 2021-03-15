from django.test import TestCase
from ..helpers.get_model import get_model
from ..models import Song, Podcast, Audiobook


class TestGetModel(TestCase):
    def setUp(self):
        self.exec = lambda file_type: get_model(file_type)

    def test_song_model(self):
        file_type = "Song"
        model = self.exec(file_type)
        self.assertEqual(model, Song)

    def test_podcast_model(self):
        file_type = "Podcast"
        model = self.exec(file_type)
        self.assertEqual(model, Podcast)

    def test_audiobook_model(self):
        file_type = "Audiobook"
        model = self.exec(file_type)
        self.assertEqual(model, Audiobook)
