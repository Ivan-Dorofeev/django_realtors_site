# Сайт риэлторского агентства
Сайт находится в разработке, поэтому доступна только страница со списком квартир и админка для наполнения БД.

Пока сайт выводит:
* Информацию по квартирам с фильтрами

![image](https://user-images.githubusercontent.com/58893102/183011383-097dfda2-ded7-4336-8273-1280b52ff589.png)

* Реализованы жалобы на квартиры

![image](https://user-images.githubusercontent.com/58893102/183011547-83153b22-7e22-4157-ac28-9aef7975c128.png)

* Нормализация номеров в админке

![image](https://user-images.githubusercontent.com/58893102/183011671-d045c89b-b7ef-4881-9451-f947ebaee600.png)

* Лайки и связи с влаельцами квартир

![image](https://user-images.githubusercontent.com/58893102/183011754-eb7e9e31-b173-4d9b-8ee5-9779cf552f07.png)



### Запуск
* Скачайте код
* Установите зависимости командой ```pip install -r requirements.txt```
* Создайте файл базы данных и сразу примените все миграции командой python3 manage.py migrate
* Запустите сервер командой ```python3 manage.py runserver```
* Переменные окружения

### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл .env рядом с manage.py и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Доступны 3 переменные:

```DEBUG``` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.

```SECRET_KEY``` — секретный ключ проекта

```ALLOWED_HOSTS``` — см документацию Django.

```DATABASE``` — однострочный адрес к базе данных, например: sqlite:///db.sqlite3. Больше информации в документации

Это позволяет легко переключаться между базами данных: PostgreSQL, MySQL, SQLite — без разницы, нужно лишь подставить нужный адрес.

### Контакты
По всем впоросам можете обратиться ко мне - контакты в шапке профиля.
