from django_filters import FilterSet # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post


# создаём фильтр
class PostSearch(FilterSet):
    # date = DateField(label='Дата')
    # text = CharField(label='Статья')
    # author = CharField(label='Автор')
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = {
            'date': ['lt'],
            # статьи позже определенной даты, что указал пользователь
            'title': ['icontains'],
            # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то что запросил пользователь
            'author': ['exact'],
            # мы хотим чтобы нам выводило имя из списка
        }
