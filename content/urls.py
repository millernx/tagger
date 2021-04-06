from django.urls import path
from . import views

app_name = "content"
urlpatterns = [
    path('', views.index, name="index"),
    path('experiment/<int:experiment_id>', views.experiment, name='experiment_detail'),
    path('vote/<int:content_id>', views.vote, name='vote'),
    #path('content/<int:content_id>', views.content, name='content_detail'),
]

