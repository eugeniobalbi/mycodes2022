# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 19:39:43 2022

@author: Eugenio B.
"""
# _________________________________________________________________
import shape_calculator
from unittest import main
# _________________________________________________________________

rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)



# _________________________________________________________________

# Correr Test
main(module='test_module', exit=False)


