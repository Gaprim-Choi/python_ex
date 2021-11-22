from my_module1 import *
from my_module2 import *

func1()
func2()
func3()

import my_area as area

print("pi=", area.PI)
print("square_area",area.square_area(5))
print("circle_area", area.circle_area(2))

from my_area import PI as pi
from my_area import square_area as sqaure
from my_area import circle_area as circle

print("pi=", pi)
print("square_area =", sqaure(5))
print("circle_area =", circle(2))