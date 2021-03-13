from django.urls import path, include
from .views import CreateView, GetView, UpdateView, DeleteView


urlpatterns = [
    path('<audioFileType>', GetView.as_view(), name='get_audio'),
    path('create/<audioFileType>', CreateView.as_view(), name='create_audio'),
    path('update/<audioFileType>/<int:audioFileID>', UpdateView, name='update_audio'),
    path('delete/<audioFileType>/<int:audioFileID>', DeleteView, name='delete_audio')
]
