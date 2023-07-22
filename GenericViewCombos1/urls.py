from django.urls import path
from GenericViewCombos1 import views



urlpatterns = [
    path('books1/', views.BookListCreateAPIView.as_view(), name='books'),
    path('books1/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view(), name='books')
]