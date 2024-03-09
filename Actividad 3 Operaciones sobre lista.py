# Usando al funcion reduce

from errno import EEXIST
from functools import reduce
from pickle import REDUCE

print(reduce(lambda a,b: a+b, range(1,11)))