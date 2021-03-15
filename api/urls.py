from django.urls import path, include
from .views import CreateView, GetView, GetAllView, UpdateView, DeleteView


urlpatterns = [
    path('create', CreateView.as_view(), name='create_audio'),
    path('<str:audioFileType>', GetAllView.as_view(), name='get_all'),
    path('<str:audioFileType>/<int:audioFileID>', GetView.as_view(), name='get_audio'),
    path('update/<str:audioFileType>/<int:audioFileID>', UpdateView.as_view(), name='update_audio'),
    path('delete/<str:audioFileType>/<int:audioFileID>', DeleteView.as_view(), name='delete_audio')
]
