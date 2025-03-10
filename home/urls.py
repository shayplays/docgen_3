from django.urls import path
from .views import generate_document, select_document, category_documents

urlpatterns = [
    path('', select_document, name='select_document'),
    path('<str:doc_type>/', generate_document, name='generate_document'),
    path('categories/<str:category_name>/', category_documents, name='category_documents'),

]