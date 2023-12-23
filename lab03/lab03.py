import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, lsim,square,sawtooth

# 生成系统模型
a = 2 * np.pi
A = [1, a]
B = [a]
sys_list = {
    'identity':lti([1],[1]),
    'default':lti(B, A),
    'low-pass':lti([1],[2,1]),
    'high-pass':lti([0.01,0],[0.01,1])
  }

# 生成信号
fs = 499
T = 1 / fs
n = np.arange(0, 1001)
t = n * T
f0_values = [1,2,5]

for name,sys in sys_list.items():
  for f0 in f0_values:
    w0 = 2 * np.pi * f0
    x = np.sin(w0 * t)
    # 信号经系统仿真
    t_out, y, x_state = lsim(sys, x, t)

    # 绘图
    plt.plot(t_out, y,label=f'Response:{name}(f={f0}Hz)')

  plt.title('System Response to Sinusoidal Input')
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.legend()
  plt.savefig(f"{name}.png", dpi=300)
  plt.show()

w1 = 2 * np.pi
x_signals = {
    'square':square(w1 * t),
    'sawtooth':sawtooth(w1 * t),
    'decay':np.exp(-t),
    'heaviside':np.where(t>=0,1,0)
  }
for key,x in x_signals.items():
  t_out, y, x_state = lsim(sys_list['default'], x, t)

  # 绘图
  plt.plot(t_out, y, label=f'Response ({key})')
  plt.plot(t_out, x, label=f'Input ({key})', linestyle=':')

  plt.title('System Response')
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.legend()
  plt.savefig(f"{key}.png", dpi=300)
  plt.show()
