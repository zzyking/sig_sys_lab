import numpy as np
import matplotlib.pyplot as plt

T = 1
T0 = T/4
w1 = (2 * np.pi) / T
N_set = [3,5,10,20,50,100]
for N in N_set:
  t = np.linspace(-T,T,1000)

  def sa(x):
    return np.sinc(x / np.pi)
  def fourier_coefficient(k, T, T0):
    if k==0:
      return 2 * T0 / T
    return (4 * T0 / T) * sa(k * w1 * T0)
  def fourier_series(t, N, T, T0):
    x_t = np.zeros_like(t)
    for k in range(N+1):
      coef = fourier_coefficient(k, T, T0)
      x_t += coef * np.cos(k * w1 * t)
    return x_t

  x_t = fourier_series(t, N, T, T0)

  plt.figure(figsize=(12, 6))
  plt.plot(t, x_t, label = f'Fourier Series (first {N})')
  plt.title('Fourier Series Approximation')
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.legend()
  plt.savefig(f"x(t)_first{N}.png", dpi=300)
  plt.show()