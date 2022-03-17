from django.urls import path
from .views import PostList, PostDetail, PostUpdateView, PostDeleteView, PostCreateView  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', PostList.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view(), name='new_detail'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('create/<int:pk>', PostUpdateView.as_view(), name='new_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='new_delete'),
    path('create/', PostCreateView.as_view(), name='new_create'),  # Ссылка на создание товара
]
