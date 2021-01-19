#!/usr/bin/env python
# -*- coding: utf-8 -*-
x = 0.00
def Restart():
  x = input('Wpisz średnią: ')
  x = float(x)
  if (x < 6.01 and x > 0.00):
   suma = x * 1300
   str(suma)
   xmax = suma + 500
   xmin = suma - 500
   xmax = str(xmax)
   xmin = str(xmin)
   print('Bieżące środki:',suma, 'zł')
   print('https://www.komputronik.pl/category/5801/komputery-pc.html?pr10%5B%5D=' + xmin + '&pr10%5B%5D=' + xmax + '&filter=1&showBuyActiveOnly=0')
   y = input('Jeśli chcesz kontynuować to napisz [Tak|Nie]')
   y = str(y)
   if (y == 'Tak'):
        Restart()
   if (y == 'Tak' or 'Nie' == False):
        print('Niezrozumiane polecenie :(')
   if (y == 'Nie'):
        print('ok')


if (x > 6.00):
   print('nie ściemnaj 6.00 jest najwięcej')
   y = input('Jeśli chcesz kontynuować to napisz [Tak|Nie]')
   y = str(y)
   if (y == 'Tak'):
      Restart()
   if (y == 'Nie'):
      print('ok')
   if (y == 'Tak' or 'Nie' == False):
    print('Niezrozumiane polecenie :(')

Restart()