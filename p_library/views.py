from django.shortcuts import render, redirect
from p_library.models import Author, Friend, Book 
from p_library.forms import AuthorForm, FriendForm, BookForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from django.forms import formset_factory  #для работы с множеством форм на странице
from django.http.response import HttpResponseRedirect

class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    # success_url = reverse_lazy('p_library:author_list')
    success_url = reverse_lazy('author_list')
    template_name = 'author_edit.html'  
    
class AuthorList(ListView):  
    model = Author  
    template_name = 'authors_list.html'

#форма создния друзей
class FriendEdit(CreateView):  
    model = Friend  
    form_class = FriendForm  
    success_url = reverse_lazy('friend_list')
    template_name = 'friends_edit.html'

class FriendList(ListView):  
    model = Friend 
    success_url = reverse_lazy('friends_books') #в случае успеха перенаправляем на страницу друзей и книг
    template_name = 'friends_list.html'
#   
class BookList(ListView):
    model = Book
    template_name = 'books_list.html'

def author_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  #  Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  #  Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  #  Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`.Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if author_formset.is_valid():  #  Проверяем, валидны ли данные формы
            for author_form in author_formset:  
                author_form.save()  #  Сохраним каждую форму в формсете
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  #  После чего, переадресуем браузер на список всех авторов.
    else:  #  Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(prefix='authors')  #  Инициализируем формсет и ниже передаём его в контекст шаблона.
    context = {'author_formset': author_formset} # обязательно должен быть словать
    return render(request, 'manage_authors.html', context)

def books_authors_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  
    BookFormSet = formset_factory(BookForm, extra=2)  
    if request.method == 'POST':  
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')  
        if author_formset.is_valid() and book_formset.is_valid():  
            for author_form in author_formset:  
                author_form.save()  
            for book_form in book_formset:  
                book_form.save()  
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  
    else:  
        author_formset = AuthorFormSet(prefix='authors')  
        book_formset = BookFormSet(prefix='books')  
    return render(
	    request,  
		'manage_books_authors.html',  
		{  
	        'author_formset': author_formset,  
			'book_formset': book_formset,  
		}  
	)

def friends_books(request):
    fr = Friend.objects.all()
    all_books = Book.objects.all()
    # if request.method != 'POST':
    #     fr = Friend.objects.all()
    context = {'fr': fr, 'all_books' : all_books}
    # return HttpResponseRedirect(reverse_lazy('p_library:friends_books'))
    return render(request, 'manage_friend_books.html', context)

def book_edit(request, book_id):
    """ редактируем книгу """
    book = Book.objects.get(id=book_id)
    fr = book.friend # ссылка на друга по внешнему ключу

    if request.method != 'POST':
        form = BookForm(instance=book) # ссылка на друга по внешнему ключу
    else:
        form = BookForm(instance=book, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    # вывести пустую или недействительную форму
    context = {'book': book, 'fr': fr, 'form' : form }
    return render(request, 'edit_book.html', context)
