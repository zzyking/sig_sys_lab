import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 定义系统类
class System:
  def __init__(self,name):
    self.numerator = []
    self.denominator = []
    self.name = name
# 根据 H(s) 得到系数矩阵
H1 = System('H1')
H1.numerator = [2]
H1.denominator = [1,2]
H2 = System('H2')
H2.numerator = [1,0]
H2.denominator = [1,2]
H3 = System('H3')
H3.numerator = [1]
H3.denominator = [1,2,10]
H4 = System('H4')
H4.numerator = [1,-3,2]
H4.denominator = [1,3,2]
sys_list = [H1,H2,H3,H4]
for sys in sys_list:
  numerator = sys.numerator
  denominator = sys.denominator

  # 通过系数矩阵定义系统
  system = signal.TransferFunction(numerator, denominator)

  # 零极点
  zeros = system.zeros
  poles = system.poles

  # 画出零极点
  plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Zeros')
  plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles')


  plt.xlim([-4, 4])
  plt.ylim([-4, 4])
  plt.grid(color = 'gray', linestyle = ':', linewidth = 0.2)
  plt.title('Pole-Zero Map')
  plt.xlabel('Real')
  plt.ylabel('Imaginary')
  plt.legend()
  plt.savefig(f"{sys.name}_pzmap.png", dpi=300)
  plt.show()

  # 计算频率响应
  frequency, response = signal.freqresp(system)

  # 画出频响曲线
  plt.figure()
  plt.plot(frequency, np.abs(response),label = f'{sys.name} Response')
  plt.title('System Frequency Response Curve')
  plt.xlabel('Frequency')
  plt.ylabel('Amplitude Response')
  plt.grid(color = 'gray', linestyle = ':', linewidth = 0.2)
  plt.legend()
  plt.savefig(f"{sys.name}_freqs.png", dpi=300)
  plt.show()