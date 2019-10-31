#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://webfanat.com/article_id/?id=142

import pyautogui

pyautogui.alert(text='Hello world', title='Приветствие', button='OK')

res = pyautogui.confirm(text='Вы заинтересованы в развитии проекта', title='Опрос', buttons=['Да','Еще не определил', 'Нет'])
print(res)

res1 = pyautogui.prompt(text='Как насчет вставать в 4 утра', title='Выскажите мнение' , default='Ни за что')
print(res1)

res2= pyautogui.password(text='Введите свой пароль', title='Аутентификация', default='', mask='*')
print(res2)