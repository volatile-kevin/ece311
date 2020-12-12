# EXERCISE 2
#Code for exercise 2:
b = [1/3, -1/9, 1, -1/9, 1/3]
a = [1, 0, 0, 0, 0]
z, p, _ = signal.tf2zpk(b,a)
n, y = signal.dimpulse((b,a,1), n=8)
h = y[0]

pz_plot(z, p, '2a. pole-zero plot')
plt.figure()
plt.stem(n, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('2a. impulse response')

b = [1, 0, 1/4]
a = [1, 1, -6]
z, p, _ = signal.tf2zpk(b,a)
n, y = signal.dimpulse((b,a,1), n=20)
h = y[0]

pz_plot(z, p, '2b. pole-zero plot')
plt.figure()
plt.stem(n, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('2b. impulse response')

b = [1, 0, -1/2]
a = [1, 0, 1]
z, p, _ = signal.tf2zpk(b,a)
n, y = signal.dimpulse((b,a,1), n=20)
h = y[0]

pz_plot(z, p, '2c. pole-zero plot')
plt.figure()
plt.stem(n, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('2c. impulse response')

# EXERCISE 4
Fs = 44100 #sampling rate for audio clip in Hz
t1 = 5 #make clips 5 seconds
t = np.linspace(0,t1,t1*Fs)
f0 = 0 #start frequency (Hz)
f1 = 22050 #end frequency (Hz)
chirp_original = signal.chirp(t,f0 = f0, t1 = t1, f1 = f1)
nfft = 1024

#Code for part 4.a:
f, t, S = signal.spectrogram(chirp_original, Fs, nperseg = nfft, noverlap = int(nfft/2), nfft = nfft)
plt.figure(figsize=(12,8))
plt.pcolormesh(t, f, sig2db(S))
plt.title('4a. spectrogram')
plt.ylim([0, 22050])
plt.ylabel('f')
plt.xlabel('t')
plt.colorbar()

#Code for part 4.b:
Fs = 8820
t2 = np.linspace(0,t1,t1*Fs)
downsample = signal.chirp(t2, f0=f0, t1=t1, f1=f1)

f, t2, S = signal.spectrogram(downsample, Fs, nperseg = nfft, noverlap = int(nfft/2), nfft = nfft)

plt.figure(figsize=(12,8))
plt.pcolormesh(t2, f, sig2db(S))
plt.title('4b. spectrogram for downsampled')
plt.ylim([0, 4410])
plt.ylabel('f')
plt.xlabel('t')
plt.colorbar()
