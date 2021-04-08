from django.urls import path

from . import views

urlpatterns = [
    path('', views.documents_list, name='index'),
    path('documents/upload/', views.upload_document, name='upload_document'),
    path('<str:file_name>/', views.filter_by_filename, name='detail'),
    path('download_document', views.download_document, name='download_document'),
]