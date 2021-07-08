from django.urls import path
import cloud.views

urlpatterns = [
    path('', cloud.views.index, name='index'),
    path('docs/', cloud.views.docs, name='docs'),
    path('pics/', cloud.views.pics, name='pics'),
]