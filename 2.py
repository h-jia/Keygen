# -*- coding: utf-8 -*-

import numpy as np
# import urandom
from os import urandom

a = np.frombuffer(urandom(5), dtype=np.uint8)
b = a.tobytes()
c = np.frombuffer(b, dtype=a.dtype)
d = np.unpackbits(c, axias=0)
print(c)
print(d)

b = bytes(str(a), 'utf8')
c = b.decode("utf-8")
print(c)