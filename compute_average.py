import numpy as np
import matplotlib.pyplot as plt
import time
import random


class Average():
    def __init__(self):
        pass

    def get_time(self):
        return time.time()

    def avg_vectorization(self, x):
        t0 = self.get_time()
        np_ones = np.ones_like(x)
        b = np.dot(np_ones.T, x)/np.linalg.norm(np_ones)**2
        t1 = self.get_time()

        return b, t1-t0


    def avg_builtin(self, x):
        t0 = self.get_time()
        avg = np.mean(x)
        t1 = self.get_time()
        return avg, t1-t0


    def avg_for_loop(self, x):
        t0 = self.get_time()
        s = 0
        for i in x:
            s += i
            avg = s/len(x)
        t1 = self.get_time()
        return avg, t1-t0


    def avg_assumedmean(self, x):
        t0 = self.get_time()
        m = random.choice(x)
        A = np.array((x-m)).sum()
        m = m + A/len(x)
        t1 = self.get_time()
        return m, t1-t0


    def avg_recursive(self, x):
	    t0 = self.get_time()
	    m_prev = x[0]
	    for k in range(1, len(x)):
		    m_new = m_prev + (x[k]-m_prev)/k
		    m_prev = m_new
	    t1 = self.get_time()
	    return m_prev, t1-t0


if __name__ == "__main__":
    n = np.arange(100, 1000, 99)
    p, q, r, s, t = np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n))
    pt, qt, rt, st, tt = np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n))
    
    a = Average()
    for i, j in enumerate(n):
        x = np.random.randint(1000, size=(j)).reshape(-1,1)
        p[i], pt[i] = a.avg_for_loop(x)
        q[i], qt[i] = a.avg_vectorization(x)
        r[i], rt[i] = a.avg_builtin(x)
        s[i], st[i] = a.avg_recursive(x)
        t[i], tt[i] = a.avg_assumedmean(x)
    
    str_legend = ['for loop', 'vectorization', 'builtin', 'recursive', 'assumed mean'] 
    fig = plt.figure(1)
    ax1 = plt.subplot(211)
    plt.plot(n, pt, 'r', n, qt, 'g', n, rt, 'b', n, st, 'm', n, tt, 'k')
    plt.title('Computation time')
    plt.grid()
    plt.legend(str_legend)
    ax2 = plt.subplot(212)
    plt.title('Average value')
    plt.plot(n, p, '*r', n, q, '*g', n, r, '*b', n, s, '*m', n, t, '*k')
    plt.legend(str_legend)
    plt.grid()
    plt.show()
