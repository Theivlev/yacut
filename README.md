# Проект YaCut и API к нему
Это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

## Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
- обязательного для длинной исходной ссылки;
- необязательного для пользовательского варианта короткой ссылки.
***
Если пользователь предложит вариант короткой ссылки, который уже занят, то нужно сообщить пользователю об этом через уведомление: Предложенный вариант короткой ссылки уже существует.Существующая в базе данных ссылка должна остаться неизменной
Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис должен сгенерировать её автоматически. Формат для ссылки по умолчанию — шесть случайных символов, в качестве которых можно использовать:
- большие латинские буквы,
- маленькие латинские буквы,
- цифры в диапазоне от 0 до 9.
> Автоматически сгенерированная короткая ссылка добавляется в базу данных, но только если в ней уже нет такого же идентификатора. В противном случае генерируется идентификатор заново.

## Примеры запросов к API, варианты ответов и ошибок приведены в спецификации openapi.yml

# Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Theivlev/yacut
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```