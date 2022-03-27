import numpy as np
import matplotlib.pyplot as plt

def Show_data(x, N, s='data'):

    # size of each sample of the timeseries
    L = 60

    # plot the first N samples
    for i in range(N):
        plt.plot(np.arange(i*L,(i+1)*L),x[i])

    plt.xlabel('time')
    plt.title(s)
    plt.show()