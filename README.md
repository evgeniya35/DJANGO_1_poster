# Афиша
Программа (сайт) для накопления и отображения на карте афишы достопримечательных мест.

[Доступна демо версия сайта](https://johnss.pythonanywhere.com/).

Для входа в административный раздел [перейдите](https://johnss.pythonanywhere.com/admin).

## Установка
Установите программу из репозитория GitHub:
```bash
git clone https://github.com/evgeniya35/DJANGO_1_poster.git

```

Установите завистимости
```bash
pip install -r requirements.txt
```

Создайте начальную базу данных:
```bash
python manage.py migrate
```

Создайте пользователя для работы с admin-разделом:
```bash
python manage.py createsuperuser
```

## Переменные окружения
Настройте переменные окружения в файле `.env` (рядом с файлом `manage.py`):
```
SECRET_KEY={Секретный ключ}
DEBUG=False
ALLOWED_HOSTS=127.0.0.1
DB_LOCATION=/home/john/PY/dvmn/DJANGO_1_poster/
```

## Запуск
Для отладкит и тестового запуска локального сервера используйте:
```bash
python manage.py runserver
```
Перейдите в административный раздел по адресу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). Заполните модели `Excursion` тестовыми данными по экскурсиям.

Отображение экскурсий на карте будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

