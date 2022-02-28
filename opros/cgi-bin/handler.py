#!/usr/bin/env python3

import cgi
import os

form = cgi.FieldStorage()

first_name = form.getvalue("first_name", "не задано")
second_name = form.getvalue("second_name", "не задано")
patronymic = form.getvalue("patronymic", "не задано")
password = form.getvalue("password", "Не задано")
choose_device = form.getvalue("Ai_think", "Не задано")
radio = form.getvalue("AI_Usage")
Sound_help = form.getvalue("Sound_help", "off")
Autocar = form.getvalue("Autocar", "off")
Amazon = form.getvalue("Amazon", "off")
GMaps = form.getvalue("GMaps", "off")

checkboxes = {"Голосовые помощники": Sound_help, "Автопилот в машине": Autocar, "Amazon": Amazon, "Google Maps": GMaps}

checkboxes_filtered = []

for key in checkboxes:
    if checkboxes[key] == "on":
        checkboxes_filtered.append(key)

checkboxes_answer = ", ".join(checkboxes_filtered)

print("Content-type: text/html; charset: utf-8\n")

print("""
<!DOCTYPE html>
<html lang="ru">
  <head>
    <title>Разработчик видеоигр</title>
    <meta charset="utf-8">
    <style type="text/css">
      #table {
        width:1000px;
        margin-bottom: 20px;
        border: 1px solid #dddddd;
       border-collapse: collapse; 
      }
      th {
        font-weight: bold;
        padding: 5px;
       background: #efefef;
        border: 1px solid #dddddd;
      }
      td {
        border: 1px solid #dddddd;
        padding: 5px;
        text-align: center;
     }
      tbody tr:nth-child(odd) {
        background-color: #C9E4F6;/* фон нечетных строк */
      }
      tbody tr:nth-child(even) {
        background-color: #B4DAF2;/* фон четных строк */
      }
    </style>
  </head>
	<body>
""")

# ----------------

print(f"""
    <h1>Анкетирование: результаты</h1>
    <table border="1" style="color: black; font-size: 20px">
      <tr>
        <th>Имя поля</th>
        <th>Значение</th>
      </tr>
      <tr>
        <td>Фамилия</td>
        <td>{second_name}</td>
      </tr>
      <tr>
        <td>Имя</td>
        <td>{first_name}</td>
      </tr>
      <tr>
        <td>Отчество</td>
        <td>{patronymic}</td>
      </tr>
      <tr>
        <td>Отношение к ИИ</td>
        <td>{choose_device}</td>
      </tr>
      <tr>
        <td>ИИ в повседневной жизни</td>
        <td>{radio}</td>
      </tr>
      <tr>
        <td>Ипользуемые системы</td>
        <td>{checkboxes_answer}</td>
      </tr>
      <tr>
        <td>Пароль</td>
        <td>{password}</td>
      </tr>
    </table>


""")

print("""
</body>
</html>
""")
