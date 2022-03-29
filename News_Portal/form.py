from django.forms import ModelForm, CharField
from .models import Post, User, Author


# Создаём модельную форму
class PostForm(ModelForm):
    # title = CharField(label='Заголовок')
    # text = CharField(label='Статья')
    # type = CharField(label='Тип')
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['title', 'text', 'type', 'author', 'category']

# Создаём модельную форму Для Авторов
class AuthorForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'