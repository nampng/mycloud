from django.urls import path
import cloud.views

urlpatterns = [
    path('', cloud.views.index, name='index'),
    path('files/', cloud.views.files, name='files'),
]