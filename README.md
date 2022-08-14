# Simple Levenshtein database <br> ![build passing](https://img.shields.io/badge/build-passing-brightgreen) ![license](https://img.shields.io/github/license/beautiful-white/simple-lev-database) ![download](https://shields.io/github/downloads/beautiful-white/simple-lev-database/total) ![checks](https://shields.io/github/checks-status/beautiful-white/simple-lev-database/b44eea2c45c08dcdea5ede4358a1920d82103b3c)
*This database has created for bot (search similar answers/questions (calls)) and simple saving data in JSON files*
## Description
Simple Levenshtein database is a DB for your bot in Python. If you don't want to use any big database (for exemple SQLite, MySQL and etc.) and integrate system of similar calls you can use this for it. Database saves all files (backups) in JSON.
## Dependecies
<b><a href="https://github.com/seatgeek/thefuzz">FuzzyWuzzy</a></b>.
## Preparation
Before using you need to install <b>datab.py</b> from this [repository](https://github.com/beautiful-white/simple-lev-database/releases) to the directory with your project.
## Usage
### Connection
Import main class Base:
```python
from datab import Base
```
For using you need to create own sample, e. g:
```python
bd = Base()
```
### General functions
There are all functions:
```python
bd.load(backup_name)
bd.update(backup_name)
bd(c_id, question)
bd(c_id, question, answer)
bd.backup()
bd.last_log(save=False)
```
### Let's analyse!
- <b>bd.load(backup_name)</b> - function for loading database from backup. It rewrites whole database by backup. *Backup_name* must be name of existing backup file, or if it empty, foo will use last made backup file.
- <b>bd.update(backup_name)</b> - function for updating database from backup. It rewrites only common information and ignores unique.
- <b>bd(c_id, question)</b> - function for making call to database part *"c_id"*. *"c_id"* means <b>client id</b>, it uses for many chats, where you need create database for every chat. If you have *only* one chat or universal base, you can use any key e.g *"main"* or *"1"*. *"question"* - is a body of call. If database has same questions, it returns back a list with lists *(for exemple [["answer1", 75], ["answer2", 90]])*, where the first is the answer itself, and the second is a match for the question in the database as a percentage.
- <b>bd(c_id, question, answer)</b> - function for making call to change the question-answer connection. It just rewrites question-answer in the database.
- <b>bd.backup()</b> - function for making and saving backup in JSON file.
- <b>bd.last_log(save=False)</b> - function for returning last backup's name. It contains in <b>*config.ini*</b> file. *"save"* is a false by default and just takes last backup's name from <b>*config.ini*</b> file, but if it is true, function saves last backup's name to <b>*config.ini*</b> file. Alse you can use it with other functions:
```python
bd.load(bd.last_log())
```
or 
```python
bd.update(bd.last_log())
```
