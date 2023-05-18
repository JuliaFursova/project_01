# -*- coding: utf-8 -*-
"""Lvl_ 2 task 2.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nBcRirjPzfRmcwBckbl5I4R0ZLUplCd8
"""

# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

month = int(input("Введите номер месяца: "))

def quarter_of(month):
  quarter = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]}
  for k, v in quarter.items():
    if month == v[0] or v[1] or v[2]:
      return(f"месяц {month} является частью {k} квартала")
    
quarter_of(month)