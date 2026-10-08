from django.urls import path
from .views import *

urlpatterns = [
    path('',get_authors),
    path('authors/create/',create_author),
    path('books/',get_books),
    path('books/create/',create_book),
    path('book/<int:pk>/',book_detail),
    path('countries/',get_countries),
    path('countries/create/',create_country),
    path('country/<int:pk>/',get_country),
]