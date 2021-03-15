from django.test import TestCase
from ..helpers import is_file_type_correct


class TestCheckFileTypeAcceptability(TestCase):
    def setUp(self):
        self.exec = lambda file_type: is_file_type_correct(file_type)
    
    def test_song_file_type(self):
        file_type = "Song"
        is_acceptable = self.exec(file_type)
        self.assertEqual(is_acceptable, True)

    def test_podcast_file_type(self):
        file_type = "Podcast"
        is_acceptable = self.exec(file_type)
        self.assertEqual(is_acceptable, True)

    def test_audiobook_file_type(self):
        file_type = "Audiobook"
        is_acceptable = self.exec(file_type)
        self.assertEqual(is_acceptable, True)
    
    def test_wrong_file_type(self):
        file_type = "ZShbdhebcjej"
        is_acceptable = self.exec(file_type)
        self.assertEqual(is_acceptable, False)
