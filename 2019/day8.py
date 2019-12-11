import numpy as np
import matplotlib.pyplot as plt

data = open('day8.input').read()
data = np.array([int(c) for c in data])


w = 25
h = 6

layers = data.shape[0] // (w*h)
data = data.reshape((layers,h,w))

d = np.zeros(data.shape)
d[np.where(data == 0)] = 1
s = d.sum(axis=-1)
s = s.sum(axis=-1)
s = np.argmin(s)
ones = np.where(data[s,:,:] == 1)
twos = np.where(data[s,:,:] == 2)
print(f'part1: {len(ones[0]) * len(twos[0])}')

final_image = np.zeros((h, w))

for i in range(h):
    for j in range(w):
        final_image[i,j] = data[np.min(np.where(data[:,i,j] != 2)), i, j]
print(final_image)
plt.spy(final_image)
plt.show()