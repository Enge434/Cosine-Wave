import numpy as np
import matplotlib.pyplot as plot

time = np.arange(0,20,0.1)
amplitude = np.cos(time)
plot.plot(time,amplitude)
plot.title('Cosine Wave')
plot.xlabel('Time')
plot.ylabel('Amplitude = cosine(time)')
plot.grid(True,which = 'both')
plot.axhline(y=0,color='b')
plot.show()