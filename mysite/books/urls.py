from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_a/', views.AuthorCreateView.as_view(), name='author_add'),
    path('a/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('add/', views.BookCreateView.as_view(), name='book_add'),
    path('<int:pk>/upd/', views.BookUpdateView.as_view(), name='book_upd'),
    path('<int:pk>/del/', views.BookDeleteView.as_view(), name='book_del'),
    path('a/<int:pk>/upd/', views.AuthorUpdateView.as_view(), name='author_upd'),
    path('a/<int:pk>/del/', views.AuthorDeleteView.as_view(), name='author_del')
]