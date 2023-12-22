import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from IPython.display import Audio

# 定义信号参数
A = 1  # 振幅
f0 = 10  # 连续信号频率
Fs = 40  # 抽样频率
T = 0.2  # 信号时间长度
t_continuous = np.arange(0, T, 0.001)  # 连续信号时间范围

# 连续信号
x_continuous = A * np.sin(2 * np.pi * f0 * t_continuous)

# 抽样过程
Fs_values = [20, 30, 50]

plt.figure(figsize=(16,9))
# 绘制连续信号
plt.subplot(4, 1, 1)
plt.plot(t_continuous, x_continuous)
plt.title('Continuous Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# 绘制抽样信号
for i, Fs in enumerate(Fs_values, start=2):
    Ts = 1 / Fs  # 抽样间隔
    n = np.arange(0, T, Ts)  # 离散时间范围
    x_sampled = A * np.sin(2 * np.pi * f0 * n * Ts)  # 离散信号

    plt.subplot(4, 1, i)
    plt.stem(n, x_sampled)
    plt.title(f'Sampled Signal (Fs={Fs} Hz)')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
