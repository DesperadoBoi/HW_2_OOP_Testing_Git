# HW_2_OOP_Testing_Git

Домашнее задание по ООП, тестированию и работе с Git/GitHub.

## Описание

В проекте реализованы классы для работы с рецептами:

- `Ingredient`
- `Recipe`
- `ShoppingList`
- `DietaryRecipe`

Для проверки работы классов написаны тесты с использованием `pytest`.

## Структура проекта

```text
src/
  recipes.py
  __init__.py

tests/
  test_recipes.py

requirements.txt
README.md
.gitignore
```

## Использование

Склонировать репозиторий:

```bash
git clone https://github.com/DesperadoBoi/HW_2_OOP_Testing_Git.git
cd HW_2_OOP_Testing_Git
```

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать виртуальное окружение на Windows:

```bash
.venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить тесты:

```bash
python -m pytest
```

Запустить основной файл с кодом:

```bash
python src/recipes.py
```

## Работа с Git

Проект ведется в публичном репозитории GitHub.

Изменения сохранялись через коммиты и отправлялись в ветку `main`.

## Автор

ФИО: `Честных Михаил Алексеевич`

Учебная группа: `ББИ 2510`