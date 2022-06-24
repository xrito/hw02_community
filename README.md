## backend_community_homework


### Описание
Создано и зарегистрировано приложение Posts.

Подключена база данных.

Десять последних записей выводятся на главную страницу.

В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие.
Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

Модели (models.py):

1. Post - запись. Поля:
  - text(текст записи) - тип поля - Текст
  - pub_date(дата публикации) - тип поля - Дата (автоматически добавляется текущая дата)
  - author(Автор) - тип поля - Ссылка на модель User (связь «один-ко-многим»)
  - group(Сообщество) - тип поля - Ссылка на модель Group (связь «один-ко-многим»)
2. Group - сообщество. Поля:
  - title(Имя) - тип поля - Строка
  - slug(Адрес) - тип поля - slug
  - description(Описание) - тип поля - Текст
  метод __str__ возвращает имя сообщества (title)
  
Админка (admin.py)

  - Зарегистрированы модели Post, Group.

  - Для модели Post создана кастомная админка:
    - В списке объектов в админке отображаются поля pk, text, pub_date, author, group.
    - Содержимое поля group можно редактировать в админке прямо в списке объектов Post.
    - Доступен поиск по полю text.
    - Доступна фильтрация по полю pub_date.
    - Если какое-то поле не заполнено, в нём отображается текст -пусто-.
    
View-функции (views.py):
  - index(): передаёт в шаблон posts/index.html десять последних объектов модели Post.
  - group_posts(): передаёт в шаблон posts/group_list.html десять последних объектов модели Post, отфильтрованных по полю group, и    содержимое для тега <title>.
 
Адреса (urls.py)
  - Для приложения Posts установлен namespace='posts'.
  - Для главной страницы установлен name='index'.
  - Страница с постами из определённой группы доступна по URL вида group/<slug>/.
  - Для страницы с постами группы установлен name='group_list'.

Шаблоны:
  - Файлы шаблонов хранятся на уровне проекта.
  - Шаблоны разбиты на логические блоки и собираются с помощью тегов include и extend.
  - К шаблонам подключена статика.
  - В шаблоне index.html все записи группы адресует пользователя на страницу той группы, которой принадлежит пост.
  - Из view-функций в словаре context передаётся основное содержимое страницы.
  - Содержимое тега <title>:
    - для страницы группы: Записи сообщества <имя_группы>;
    - для главной страницы: Последние обновления на сайте.


### Стек
+ Python 3.7 
+ Django 2.2.19

### Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/xrito/hw02_community
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
source env/bin/activate
```

Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Запустить проект:
```
python3 manage.py runserver
```

### Автор
[![Telegram](https://img.shields.io/badge/-Telegram-464646?style=flat-square&logo=Telegram)](https://t.me/harkort)
[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/xrito)  


[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![pytest](https://img.shields.io/badge/-pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?style=flat-square&logo=SQLite)](https://www.sqlite.org/)
