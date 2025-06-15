import numpy as np

f = lambda x: np.exp(-x)
exact = 1 - np.exp(-5)

def trapezoidal(a, b, n):
    h = (b - a)/n
    x = np.linspace(a, b, n+1)
    return h*(np.sum(f(x)) - (f(a) + f(b))/2)

def romberg(a, b, max_i=20, tol=1e-6):
    R = np.zeros((max_i, max_i))
    R[0, 0] = (f(a) + f(b)) * (b - a)/2
    
    for i in range(1, max_i):
        h = (b - a)/2**i
        R[i, 0] = 0.5*R[i-1, 0] + h*np.sum(f(a + np.arange(1, 2**i, 2)*h))
        
        for j in range(1, i+1):
            R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1])/(4**j - 1)
        
        if i > 0 and abs(R[i, i] - R[i-1, i-1]) < tol:
            return R[i, i], i+1
    
    return R[-1, -1], max_i

a, b, n = 0, 5, 100
trap = trapezoidal(a, b, n)
rom, iter_ = romberg(a, b)

print(f"Integral dari e^(-x) dalam interval [0, 5]\nNilai eksak: {exact:.10f}\n"
      f"\nMetode Trapezoidal:\nHasil: {trap:.10f}\nError: {abs(trap-exact):.10f}\nJumlah interval: {n}"
      f"\n\nMetode Romberg:\nHasil: {rom:.10f}\nError: {abs(rom-exact):.10f}\nJumlah iterasi: {iter_}"
      f"\n\nPerbandingan:\nSelisih hasil: {abs(trap-rom):.10f}\n"
      f"Romberg {abs(rom-exact)/abs(trap-exact)*100:.5f}% lebih akurat dari Trapezoidal")