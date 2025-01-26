from django.urls import path
from .views import generate_document, select_document

urlpatterns = [
    path('', select_document, name='select_document'),
    path('<str:doc_type>/', generate_document, name='generate_document'),
]