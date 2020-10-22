import numpy as np
import matplotlib.pyplot as plt
import time

def avg_np(x):
    t0 = time.time()
    a = np.ones_like(x)
    b = np.dot(a.T, x)/np.linalg.norm(a)**2
    t1 = time.time()
    return b, t1-t0

def avg_builtin(x):
    t0 = time.time()
    avg = np.mean(x)
    t1 = time.time()
    return avg, t1-t0


def avg_for_loop(x):
    t0 = time.time()
    s = 0
    for i in x:
        s += i
        avg = s/len(x)
    t1 = time.time()
    return avg, t1-t0


def avg_recursive(x):
	t0 = time.time()
	m_prev = x[0]
	for k in range(1, len(x)):
		m_new = m_prev + (x[k]-m_prev)/k
		m_prev = m_new
	t1 = time.time()
	return m_prev, t1-t0


if __name__ == "__main__":
    n = np.arange(100, 1000, 99)
    p, q, r, s = np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n))
    pt, qt, rt, st = np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n)), np.zeros(len(n))

    for i, j in enumerate(n):
        x = np.random.randint(1000, size=(j)).reshape(-1,1)
        p[i], pt[i] = avg_for(x)
        q[i], qt[i] = avg_np(x)
        r[i], rt[i] = avg_builtin(x)
        s[i], st[i] = avg_recursive(x)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(n, pt, 'r', n, qt, 'g', n, rt, 'b', n, st, 'm')
    plt.title('Time for computation')
    plt.legend(['for loop', 'numpy', 'builtin', 'recursive'])
    plt.subplot(212)
    plt.title('Average value')
    plt.plot(n, p, '*r', n, q, '*g', n, r, '*b', n, s, '*m')
    plt.legend(['for loop', 'numpy', 'builtin', 'recursion'])
    plt.show()
