# -*- coding: utf-8 -*-

import numpy as np
# import urandom

from os import urandom

a = np.frombuffer(urandom(5), dtype=np.uint8)
b = a.tobytes()
# print(type(a))
print(a)
# print(type(b))
print(b)
c = np.frombuffer(b, dtype=a.dtype)
# print(b.decode("utf-8"))
print(c)
