import numpy as np
import matplotlib.pyplot as plt

# 定义抽样间隔和时间范围
Ts_values = [0.01, 0.05, 0.1, 0.2, 0.5]
t_continuous = np.arange(0, 10, 0.001)  # 连续信号的时间范围

# 定义连续信号 xa(t) 和 ha(t)
def xa(t):
    return np.heaviside(t, 1) - np.heaviside(t - 1, 1)

def ha(t):
    return np.exp(-t) * np.heaviside(t, 1)

# 定义解析法求出的 ya(t)
def ya(t):
    return (1 - np.exp(-t)) * (np.heaviside(t, 1)-np.heaviside(t-1,1)) + (np.exp(1) - 1) * np.exp(-t) * np.heaviside(t - 1, 1)

# 定义抽样信号 xn 和 hn
def xn(n, Ts):
    return xa(n * Ts)

def hn(n, Ts):
    return ha(n * Ts)

# 定义卷积的近似计算
def convolution_approximation(x, h, Ts):
    return Ts * np.convolve(x, h, 'same')

# 画出原函数的图像
plt.figure(figsize=(8, 6))

# 绘制 xa(t) 和 ha(t)
plt.plot(t_continuous, xa(t_continuous), label='xa(t)')
plt.plot(t_continuous, ha(t_continuous), label='ha(t)')
plt.title('Original Functions')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.savefig("Original.png", dpi=300)
# 显示图形
plt.show()



# 画图比较解析法和数值方法的结果
plt.figure(figsize=(12, 8))

# 绘制解析法的结果 ya(t)
plt.plot(t_continuous, ya(t_continuous), label='Analytical Solution',linewidth = 2)


# 绘制数值法结果
y_approximations = []
for Ts in Ts_values:
    n = np.arange(int(10 / Ts) + 1)
    x_n = xn(n,Ts)
    h_n = hn(n,Ts)

    # 进行离散卷积
    y_n = np.convolve(x_n, h_n, mode='full') * Ts
    t_n = np.arange(len(y_n)) * Ts

    # 插值到连续时间
    y_interp = np.interp(t_continuous, t_n, y_n)
    y_approximations.append(y_interp)

for i, Ts in enumerate(Ts_values):
    plt.plot(t_continuous, y_approximations[i], label=f'Approximation (Ts={Ts})',linestyle='--')

plt.title('Comparison of Analytical and Numerical Solution')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.savefig("Conv.png", dpi=300)
plt.show()
