# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# owner: https://github.com/beautiful-white
# GPL-2.0 License
# 2022 © Beautiful-White

import json
import time
from fuzzywuzzy import fuzz
import os

class Base(object):

    db = {}

    last_backup = None

    debug = False
    
    def backup(self):
        if not os.path.exists("backups"):
            os.makedirs("backups")
        nm = fr".\backups\backup_{round(time.time())}.db"
        with open(nm, "w")as bk:
            bk.write(json.dumps(self.db, ensure_ascii=False))
            print("[!] Успешный бэкап базы данных!")
            self.last_backup = nm
            self.last_log(save=True)
            print(f"    {nm}")if self.debug else 1


    def update(self, name=""):
        if not name: return print("[!] Вы не ввели имя бэкапа")
        print(r"[!] Загрука апдейта {0}".format(name.replace(".db", '') + ".db"))
        try:
            with open(name.replace(".db", '') + ".db", "r", encoding="utf-8") as data:
                m = json.loads(data.read())
                for i in (set(m.keys()) & set(self.db.keys())):
                    self.db[i] = m[i]
                return print("[!] Успешная загрузка апдейта для данных!")
        except FileNotFoundError:
            name = name.replace(".db", '') + ".db"
            try:
                with open(r".\backups\\"+(name.replace(r".\backups\\", '')), "r", encoding="utf-8") as data:
                    m = json.loads(data.read())
                    for i in (set(m.keys()) & set(self.db.keys())):
                        for j in (set(m[i].keys()) & set(self.db[i].keys())):
                            self.db[i][j] = m[i][j]
                    return print("[!] Успешная загрузка апдейта для данных!")
            except FileNotFoundError:
                return print('''[!] Файл апдейта с таким именем не найден в директории БД!''')

    def load(self, name=self.last_backup):
        if not name: return print("[!] Вы не ввели имя бэкапа")
        print(r"[!] Загрука бэкапа {0}".format(name.replace(".db", '') + ".db"))
        try:
            with open(name.replace(".db", '') + ".db", "r", encoding="utf-8") as data:
                self.db = json.loads(data.read())
                return print("[!] Успешная загрузка бэкапа данных!")
        except FileNotFoundError:
            name = name.replace(".db", '') + ".db"
            try:
                with open(r".\backups\\"+(name.replace(r".\backups\\", '')), "r", encoding="utf-8") as data:
                    self.db = json.loads(data.read())
                    return print("[!] Успешная загрузка бэкапа данных!")
            except FileNotFoundError:
                return print('''[!] Бэкап с таким именем не найден в директории БД!''')

    def last_log(self, save=False):
        if not save:
            try:
                with open("config.ini", "r") as d:
                    self.last_backup = d.read()
                    return self.last_backup
            except FileNotFoundError:
                return False
        else:
            with open("config.ini", "w") as d:
                d.write(self.last_backup)
    
    def print_percent(self, l):
        print("[!] На запрос было отвечено:")
        print(l)
        for i in l:
                print(f"{i[0]} - {i[1]}% совпадения")
        if l == [[]]:
            print("[!] Совпадений не найдено!") 

    def __init__(self):
        print("[!] База данных подключена")
        self.load(self.last_log())

    def __call__(self, c_id, sent, ans=""):
        c_id = str(c_id)
        if type(self.db.get(c_id)) != dict:
            self.db[c_id] = dict()
        sent = sent.lower()
        sent = sent.split()
        #sent.sort()
        sent = "".join(sent)
        if not ans:
            qwe = []
            for i in self.db[c_id].keys():
                qwe.append([i, fuzz.ratio(i, sent)])
            qwe = list(filter(lambda x: x[1] >= 70, qwe))
            return qwe
            #for i in sent:
            #    qwe.append(list(filter(lambda x: x[1] >= 70, process.extract(i, list(self.db.keys())))))
            #self.print_percent(qwe)
        else:
            self.db[c_id][sent] = ans
            print(f'''[!] ДБ обновлена
    "{sent}" = "{ans}"''') if self.debug else 1

    
            
        
        







if __name__ == "__main__":
    print("База данных не является исполняемой часть проекта!")
    exit()
    
