import numpy as np
import matplotlib.pyplot as plt

N_set = [3,5,10,20,50,100]
for N in N_set:
  t = np.linspace(-1,1,1000)

  def sa(x):
    return np.sinc(x / np.pi)
  def fourier_coefficient(k):
    if k==0:
      return 0.5
    return 1 / (2+0.4j*k*np.pi) * sa(k * np.pi / 2)

  def fourier_series(t, N):
    y_t = np.zeros_like(t,dtype=complex)
    for k in range(-N,N+1):
      coef = fourier_coefficient(k)
      y_t += coef * np.exp(1j * k * 2 * np.pi * t)
    return np.real(y_t)

  y_t = fourier_series(t, N)

  plt.figure(figsize=(12, 6))
  plt.plot(t, y_t, label = f'Fourier Series (first {N})')
  plt.title('Fourier Series Approximation')
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.legend()
  plt.savefig(f"y(t)_first{N}.png", dpi=300)
  plt.show()