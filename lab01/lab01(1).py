import numpy as np
import matplotlib.pyplot as plt
# 信号参数
f_continuous = 5.0  # 连续信号的频率
duration = 0.201  # 信号的时长（秒）

# 抽样频率列表
sampling_rates = [20, 30, 40, 50]

# 时间范围
t_continuous = np.arange(0, duration, 1 / 1000)  # 连续信号的时间范围

# 创建一个函数，用于生成正弦信号
def generate_continuous_signal(frequency, t_continuous):
    return np.sin(2 * np.pi * frequency * t_continuous)
# 画图

# 绘制连续信号
plt.plot(t_continuous, generate_continuous_signal(f_continuous, t_continuous), label='Continuous Signal')
plt.title('Continuous Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

# 绘制离散信号
for i, rate in enumerate(sampling_rates):
    t_discrete = np.arange(0, duration, 1 / rate)  # 离散信号的时间范围
    plt.plot()
    plt.stem(t_discrete, generate_continuous_signal(f_continuous, t_discrete), label=f'Sampled Signal ({rate} Hz)')
    plt.title(f'Sampled Signal ({rate} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

