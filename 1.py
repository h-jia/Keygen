import pickle
import numpy as np

with open('key', 'rb') as file:
    key = pickle.load(file, encoding='bytes')

with open('r_key', 'rb') as file:
    r_key = pickle.load(file, encoding='bytes')

print(np.frombuffer(key, dtype=np.uint8))
print(np.frombuffer(r_key, dtype=np.uint8))

# test git commit 