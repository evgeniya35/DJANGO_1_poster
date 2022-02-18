# Афиша
Программа (сайт) для накопления и отображения на карте афишы достопримечательных мест.

[Доступна демо версия сайта](https://johnss.pythonanywhere.com/).

Для входа в административный раздел [перейдите](https://johnss.pythonanywhere.com/admin).

## Установка
Установите программу из репозитория GitHub:
```bash
git clone https://github.com/evgeniya35/DJANGO_1_poster.git

```

Установите зависимости
```bash
pip install -r requirements.txtAdd 
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
Для отладки и тестового запуска локального сервера используйте:
```bash
python manage.py runserver
```
Перейдите в административный раздел по адресу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). Заполните модели `Excursion` тестовыми данными по экскурсиям.

Отображение экскурсий на карте будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Загрузить данные
Программа умеет загружать данные в афишу достопримечательных мест из JSON файла формата:
```
{
    "title": "Горбовская ГЭС",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/151dc8d2833276130c3dff6dd1e43aac.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/5aca226c55eb7dc89d4d7547aea9bc01.jpg"
    ],
    "description_short": "В 80 километрах от Москвы стоит Горбовская ГЭС — заброшенная станция, где отлично сохранились механизмы плотины, фильтры и даже загадочный тоннель, о предназначении которого до сих пор ходят легенды. Горбовская ГЭС сегодня — это своеобразный музей раритетных конструкций.",
    "description_long": "<p>Горбовская ГЭС была сооружена в 1953 году. Она была достаточно мощной, на её борту установили два 250-киловатных генератора, а также фильтры, которые и сейчас можно увидеть, ...",
    "coordinates": {
        "lng": "36.26108899999998",
        "lat": "55.65323799999996"
    }
}


```
Для загрузки используйте команду:
```bash
python manage.py load_place {URLFile1 URLFile2 URLFile3 ..}
```
Пример команды с несколькими url можно взять из файла `places_urls.txt`

Файлы с данными можно взять [здесь](https://github.com/devmanorg/where-to-go-places.git).


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
