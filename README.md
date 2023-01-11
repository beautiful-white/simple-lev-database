## [На русском](https://github.com/beautiful-white/simple-lev-database/tree/main#простая-база-данных-с-встроенным-поиском-похожих-вопросов-основанным-на-теории-растояний-левенштайна---)

# Simple Levenshtein database <br> ![build passing](https://img.shields.io/badge/build-passing-brightgreen) ![license](https://img.shields.io/github/license/beautiful-white/simple-lev-database)
*This database has created for bot (search similar questions/answers (calls)) and simple saving data in JSON files*
## Description
Simple Levenshtein database is a DB for your bot in Python. If you don't want to use any big database (for exemple SQLite, MySQL and etc.) and integrate system of similar calls you can use this for it. Database saves all files (backups) in JSON.
## Dependecies
<b><a href="https://github.com/seatgeek/thefuzz">FuzzyWuzzy</a></b>.
## Preparation
Before using you need to install <b>datab.py</b> from this [repository](https://github.com/beautiful-white/simple-lev-database/releases) to the directory with your project.
## Usage
### Importing
Import main class Base:
```python
from datab import Base
```
For using you need to create own sample, e. g:
```python
bd = Base()
```
### General functions
List of functions:
```python
bd.load(<backup_name>)
bd.update(<backup_name>)
bd(<c_id>, <question>)
bd(<c_id>, <question>, <answer>)
bd.backup()
bd.last_log(<save=False>)
```
### Let's analyse!
- <b>bd.load(<backup_name>)</b> - function for loading database from backup. It rewrites whole database by backup. *<backup_name>* must be name of existing backup file, or if it empty, foo will use last made backup file.
- <b>bd.update(<backup_name>)</b> - function for updating database from backup. It rewrites only common information and ignores unique.
- <b>bd(<c_id>, <question>)</b> - function for making call to database part *<c_id>*. *<c_id>* means <b>client id</b>, it uses for many chats, where you need create database for every chat. If you have *only* one chat or universal base, you can use any key e.g *"main"* or *"1"*. *"question"* - is a body of call. If database has same questions, it returns back a list with lists *(for exemple [["answer1", 75], ["answer2", 90]])*, where the first is the answer itself, and the second is a match for the question in the database as a percentage.
- <b>bd(<c_id>, <question>, <answer>)</b> - function for making call to change the question-answer connection. It just rewrites question-answer in the database.
- <b>bd.backup()</b> - function for making and saving backup in JSON file.
- <b>bd.last_log(<save=False>)</b> - function for returning last backup's name. It contains in <b>*config.ini*</b> file. *<save>* is a false by default and just takes last backup's name from <b>*config.ini*</b> file, but if it is true, function saves last backup's name to <b>*config.ini*</b> file. Alse you can use it with other functions:
```python
bd.load(bd.last_log())
```
or 
```python
bd.update(bd.last_log())
```

# Простая база данных с встроенным поиском похожих вопросов, основанным на теории растояний Левенштайна <br> ![build passing](https://img.shields.io/badge/build-passing-brightgreen) ![license](https://img.shields.io/github/license/beautiful-white/simple-lev-database) 
*Эта база данных создана для ботов (поиск похожих вопросов/ответов (вызовов)) и простого экспорта данных (бэкапов) в JSON.*
## Описание
Простая база данных Левенштайна - это база для Вашего бота на Python. Если Вы не хотите использовать какие-либо тяжелые базы данных (например, SQLite, MySQL и т.д.) из-за своей нецелесообразности и интегрировать в них систему похожих вызовов - эта репозиторий для Вас. Все экспортируемые файлы базы идут в формате JSON.
## Зависимости
<b><a href="https://github.com/seatgeek/thefuzz">FuzzyWuzzy</a></b>.
## Подготовка
Перед использованием нужно установить <b>datab.py</b> отсюда [тык](https://github.com/beautiful-white/simple-lev-database/releases) в директорию с вашим проектом.
## Использование
### Ипортирование
Импортируйте главный класс Base:
```python
from datab import Base
```
Для использования базы в полной мере нужно создать свой экземпляр класса, например:
```python
bd = Base()
```
### Основной функционал
Список функций:
```python
bd.load(<backup_name>)
bd.update(<backup_name>)
bd(<c_id>, <question>)
bd(<c_id>, <question>, <answer>)
bd.backup()
bd.last_log(<save=False>)
```
### Давайте разбирать!
- <b>bd.load(<backup_name>)</b> - функция загрузки бэкапа в базу. Полностью перезаписывает всю базу. *<backup_name>* должен быть названием существующего бэкапа, если оставить пустым, функция загрузит последний сделанный бэкап.
- <b>bd.update(<backup_name>)</b> - функция обновления базы. Она переписывает лишь те данные из бэкапа, которые имеются и в нем, и в самой базе данных, тем самым не трогает уникальную информацию в базе.
- <b>bd(<c_id>, <question>)</b> - функция для запроса в базу данных *<c_id>*. *<c_id>* означает <b>client id</b>, оно используется для разных чатов, если Вам нужна отдельная база для каждого из них. Если у Вас *только* один чат или Вы хотите универсальную базу, Вы можете использовать такой вариант, как *"main"* or *"1"*. *<question>* - это тело запроса. Если база имеет схожие запросы с ответами, она вернёт список списков *(например, [["ответ1", 75], ["ответ2", 90]])*, где первое значение - ответ, а второе - совпадение запроса с имеющимся в процентном соотношении.
- <b>bd(<c_id>, <question>)</b> - функция прямого изменения связки вопроса-ответа в базе. Просто перезаписывает.
- <b>bd.backup()</b> - функция экспорта данных ввиде бэкапа формата JSON.
- <b>bd.last_log(<save=False>)</b> - функция, которая возвращает имя последнего бэкапа. Оно содержится в  <b>*config.ini*</b> файле. *<save>* по умолчанию False и берёт имя последнего бэкапа из файла <b>*config.ini*</b>, но если оно True, то функция сохранит имя послденего бэкапа в <b>*config.ini*</b>. Естественно данную функцию можно использовать в связке с другими, например:
```python
bd.load(bd.last_log())
```
или
```python
bd.update(bd.last_log())
```

