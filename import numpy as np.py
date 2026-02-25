import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Simulated data for undamaged and damaged structures (e.g., vibration data)
# Assuming vibration data is collected from sensors in time domain
sampling_rate = 1000  # Hz
t = np.linspace(0, 1, sampling_rate, endpoint=False)

# Generate undamaged structure vibration data (clean sinusoidal data)
freq_undamaged = 50  # Hz
amplitude_undamaged = 1.0
vibration_undamaged = amplitude_undamaged * np.sin(2 * np.pi * freq_undamaged * t)

# Simulated damaged structure vibration data (slight shift in frequency)
freq_damaged = 45  # Hz
amplitude_damaged = 1.2
vibration_damaged = amplitude_damaged * np.sin(2 * np.pi * freq_damaged * t)

# Perform FFT to convert time-domain data to frequency domain
fft_undamaged = fft(vibration_undamaged)
fft_damaged = fft(vibration_damaged)

# Frequency axis
freqs = fftfreq(sampling_rate, 1 / sampling_rate)

# Plotting the results for visual comparison
plt.figure(figsize=(12, 6))

# Undamaged structure FFT plot
plt.subplot(1, 2, 1)
plt.plot(freqs[:sampling_rate // 2], np.abs(fft_undamaged[:sampling_rate // 2]), color='blue')
plt.title('Undamaged Structure - Frequency Domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

# Damaged structure FFT plot
plt.subplot(1, 2, 2)
plt.plot(freqs[:sampling_rate // 2], np.abs(fft_damaged[:sampling_rate // 2]), color='red')
plt.title('Damaged Structure - Frequency Domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Compare modal frequencies
dominant_freq_undamaged = freqs[np.argmax(np.abs(fft_undamaged))]
dominant_freq_damaged = freqs[np.argmax(np.abs(fft_damaged))]

print(f"Undamaged Structure Dominant Frequency: {dominant_freq_undamaged} Hz")
print(f"Damaged Structure Dominant Frequency: {dominant_freq_damaged} Hz")

# Check if there's a significant frequency shift
if abs(dominant_freq_undamaged - dominant_freq_damaged) > 2:  # Threshold can vary
    print("Potential structural damage detected due to frequency shift.")
else:
    print("No significant structural damage detected.")