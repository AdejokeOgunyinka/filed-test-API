from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
from ..models import Song, Podcast, Audiobook


class TestUpdate(APITestCase):
    def setUp(self):
        self.song1 = Song.objects.create(name="L'oreille", duration=7000, upload_time=datetime.now())
        self.song2 = Song.objects.create(name="Enigma", duration=5000, upload_time=datetime.now())
        self.podcast1 = Podcast.objects.create(name="Grumpy Grandpa", duration=7000, upload_time=datetime.now(),
                               host="Adejoke Ogunyinka", participants=["Tito", "Williams"] )
        self.podcast2 = Podcast.objects.create(name="Game of Grandpas", duration=5000, upload_time=datetime.now(),
                               host="Adejoke Arinola", participants=["Tito", "Williams"] )
        self.audiobook1 = Audiobook.objects.create(title="Dreams with Diane", duration=7000, upload_time=datetime.now(),
                                author="Adejoke Ogunyinka", narrator="Tito Williams")
        self.audiobook2 = Audiobook.objects.create(title="Dealing with Tom", duration=5000, upload_time=datetime.now(),
                                author="Serena W.", narrator="Tito Williams")

    def test_update_song_with_id(self):
        url = reverse('update_audio', args=["Song", self.song1.id])
        data = { "name": "Le Cheveux", "duration": "3000", "upload_time": datetime.now() }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Song.objects.get(id=self.song1.id).name, "Le Cheveux")


    def test_update_podcast_with_id(self):
        url = reverse('update_audio', args=["Podcast", self.podcast1.id])
        data = { "name": "Grumpy Grandpa", "duration": 2000, "upload_time": datetime.now(), 
        "host": "Adejoke Ogunyinka", "participants": ["Tito", "Williams"] }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Podcast.objects.get(id=self.podcast1.id).duration, 2000)


    def test_update_audiobook_with_id(self):
        url = reverse('update_audio', args=["Audiobook", self.audiobook1.id])
        data = { "title": "Dreams with Diane", "duration": 7000, "upload_time": datetime.now(), 
        "author": "Adejoke Ogunyinka", "narrator": "Tito Shan" }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Audiobook.objects.get(id=self.audiobook1.id).narrator, "Tito Shan")
