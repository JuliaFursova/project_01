# -*- coding: utf-8 -*-
"""3.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RZCptLSkWA7k2YdlpdsdikxrZEl5G1q-
"""

# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

from pprint import pprint

class Matrix:
  
  def __init__(self, col, row, cell):
    self.col = col
    self.row = row
    self.cell = cell
    self.matrix = [[cell for i in range(col)] for j in range(row)]
    pprint(self.matrix)

  def new_value(self, v):
    matrix = [[v for i in range(self.col)] for j in range(self.row)]
    self.matrix = matrix
    pprint(self.matrix)

  def m_print(self):
     pprint(self.matrix)
     print(f'Количество строк = {self.row}, Количество колонок = {self.col}')

   
m = Matrix(10, 10, 5)
m.new_value(2)
m.m_print()