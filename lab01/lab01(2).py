import numpy as np
import matplotlib.pyplot as plt
import simpleaudio as sa

duration = 1  # 信号的时长（秒）
def generate_piano_note(frequency, duration, sampling_rate):
  t_discrete = np.arange(0, duration, 1 / sampling_rate)
  note_signal = 0.5 * np.sin(2 * np.pi * frequency * t_discrete)
  return note_signal


# 钢琴音符频率
piano_notes = {'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00, 'A4': 440.00, 'B4': 493.88}

for selected_note in piano_notes.keys():
  # 选取一个音符
  selected_frequency = piano_notes[selected_note]

  # 生成并播放音符信号
  note_signal = generate_piano_note(selected_frequency, duration, 8000)
  play_obj = sa.play_buffer((note_signal * 32767).astype(np.int16), 1, 2, 8000)
  play_obj.wait_done()

  if selected_note == 'C4':
    # 绘制音符信号波形图
    plt.plot(note_signal)
    plt.title(f'{selected_note} Note Signal')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.xlim(0, 25)
    plt.show()
