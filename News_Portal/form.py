from django.forms import ModelForm, CharField, ModelChoiceField
from .models import Post, User, Author, Category


# Создаём модельную форму
class PostForm(ModelForm):
    # title = CharField(label='Заголовок')
    # text = CharField(label='Статья')
    # type = CharField(label='Тип')
    # мы хотим чтобы нам выводило категория списком
    category = ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория'
    )
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['title', 'text', 'type', 'author', 'category']

# Создаём модельную форму Для Авторов
class AuthorForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'