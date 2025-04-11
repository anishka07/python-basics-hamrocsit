# default module of python
import os # import the default os module

# installed modules
# import numpy as np # alias numpy to np
# import pandas as pd # alias pandas to pd

from mymodule import myname as nickname # alias 
from mymodule import greetings, saymyname # import specific functions not all

print(os.getcwd())

greeting = greetings("World")
print(greeting)

name = saymyname("Heisenberg")
print(name)

name = saymyname(nickname)
print(name)
