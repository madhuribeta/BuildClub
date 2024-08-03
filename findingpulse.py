# Step 1: Import necessary packages
import cv2
from scipy.fft import rfft, rfftfreq, irfft
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Read frames from the input video and collect the green channel
video_path = 'video_path.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

green_channel_list = []
fps = cap.get(cv2.CAP_PROP_FPS)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    green_channel = frame[:, :, 1]  # Extract green channel
    green_channel_mean = np.mean(green_channel)
    green_channel_list.append(green_channel_mean)

cap.release()

# Step 3: Mean normalize the pixel values (Green Channel)
green_channel_array = np.array(green_channel_list)
mean_value = np.mean(green_channel_array)
normalized_signal = green_channel_array - mean_value

# Plot the normalized signal
plt.figure(figsize=(10, 4))
plt.plot(normalized_signal)
plt.title('Mean Normalized Green Channel Signal')
plt.xlabel('Frame')
plt.ylabel('Intensity')
plt.show()

# Step 4: Apply Fast Fourier Transform (FFT) on the signal
fft_signal = rfft(normalized_signal)
fft_freq = rfftfreq(len(normalized_signal), 1/fps)

# Plot the FFT of the signal
plt.figure(figsize=(10, 4))
plt.plot(fft_freq, np.abs(fft_signal))
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

# Step 5: Filter out frequencies outside the human pulse range
low_cutoff = 0.45  # 27 bpm
high_cutoff = 8.0  # 480 bpm

filtered_signal = np.copy(fft_signal)
filtered_signal[(fft_freq < low_cutoff) | (fft_freq > high_cutoff)] = 0

# Plot the filtered FFT of the
