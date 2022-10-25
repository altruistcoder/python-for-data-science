import matplotlib.pyplot as plt 
import numpy as np 

np.random.seed(0) 
  
d = 0.01 

Fs = 1 / d

temp = np.arange(0, 10, d) 
res = np.random.randn(len(temp)) 
r = np.exp(-temp / 0.05)
conv_res = np.convolve(res, r)*d
conv_res = conv_res[:len(temp)] 
s = 0.5 * np.sin(1.5 * np.pi * temp) + conv_res
fig, (ax) = plt.subplots() 
ax.plot(temp, s) 
ax.phase_spectrum(s, Fs = Fs)

plt.title(“Spectrum Plot”)
plt.show()
