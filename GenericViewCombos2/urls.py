from django.urls import path
from GenericViewCombos2 import views



urlpatterns = [
    path('books2/', views.BookListCreateAPIView2.as_view(), name='books'),
    path('books2/<int:pk>/', views.BookRetrieveUpdateDestroy2.as_view(), name='books')

]