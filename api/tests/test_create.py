from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
from ..models import Song, Podcast, Audiobook


class TestCreate(APITestCase):
    def test_create_song(self):
        url = reverse('create_audio')
        data = { "audioFileType": "Song", "audioFileMetadata": { "name": "L'oreille",
                "duration": 7000, "upload_time": datetime.now() }}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(Song.objects.get(id=1).name, "L'oreille")

    def test_create_podcast(self):
        url = reverse('create_audio')
        data = { "audioFileType": "Podcast", "audioFileMetadata": { "name": "Grumpy Grandpa",
                "duration": 7000, "upload_time": datetime.now(), "host": "Adejoke Ogunyinka",
                "participants": ["Tito", "Williams"] }}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Podcast.objects.count(), 1)
        self.assertEqual(Podcast.objects.get(id=1).host, "Adejoke Ogunyinka")

    def test_create_audiobook(self):
        url = reverse('create_audio')
        data = { "audioFileType": "Audiobook", "audioFileMetadata": { "title": "Dreams with Diane",
                "duration": 7000, "upload_time": datetime.now(), "author": "Adejoke Ogunyinka",
                "narrator": "Tito Williams" }}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Audiobook.objects.count(), 1)
        self.assertEqual(Audiobook.objects.get(
            id=1).title, "Dreams with Diane")
