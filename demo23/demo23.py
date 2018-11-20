import sys  # Built in Function
import sample

print(sys.path)
print(sample.add(3, 5))
print(sample.subtract(5, 3))


'''

Above is a wrong way to handle any package.
Developer must structure the code in a way that the functions used in a script is know to all

GOOD Practice:

from sample import add,subtract

BAD Practice :

import sample 

OR

from sample import *


'''
