"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  
from django.urls import path  
from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, FriendList, FriendEdit, friends_books, BookList, book_edit
  
app_name = 'p_library'  
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'), #books_authors_create_many вызываем метод из файла view.py
    path('friends', FriendList.as_view(), name='friend_list'), # выводим список друзей и переходим в форму создания друга и форму выдачи книг друзьям
    path('friend/create', FriendEdit.as_view(), name='friend_create'), # формма создания друга
    path('friends/books', friends_books, name='friends_books'), # формма создания друга
    path('books', BookList.as_view(), name='books_list'), # форма просмотра всех книг с уточнением, у кого книга. 
    path('book/edit/<int:book_id>/', book_edit, name='book_edit'), # форма редактирования книги, можно отдать книгу другу
]
