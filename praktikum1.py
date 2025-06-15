import matplotlib.pyplot as plt
import numpy as np
import math

# BOLEH DIUBAH YA
def f(x):
    return math.cos(x) - 3*x
x1 = 0.3
x2 = 0.4

    # Contoh Soal 1:
    # return math.sin(x) - 5*x + 2
    # x1 = 0.4
    # x2 = 0.5

    # Contoh Soal 2:
    # return math.exp(x) - 2*x - 21
    # x1 = 3
    # x2 = 4

    # Contoh Soal 3:
    # return math.cos(x) - 3*x
    # x1 = 0.3
    # x2 = 0.4



tol = 1e-5
max_iter = 100

def regula_falsi(f, x1, x2, tol=1e-5, max_iter=100):
    if f(x1) * f(x2) >= 0:
        print(f"Metode gagal: f({x1}) = {f(x1):.6f}, f({x2}) = {f(x2):.6f}")
        print("f(x1) dan f(x2) harus memiliki tanda yang berbeda.")
        return None

    print("{:<8} {:<12} {:<12} {:<12} {:<12}".format("Iterasi", "x1", "x2", "x3", "f(x3)"))
    for i in range(max_iter):
        f1 = f(x1)
        f2 = f(x2)
        x3 = x2 - f2 * (x1 - x2) / (f1 - f2)
        f3 = f(x3)
        print("{:<8} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(i + 1, x1, x2, x3, f3))

        if abs(f3) < tol:
            return x3

        if f1 * f3 < 0:
            x2 = x3
        else:
            x1 = x3

    return x3

akar = regula_falsi(f, x1, x2, tol, max_iter)
if akar is not None:
    print("\nAkar ditemukan pada x = {:.6f}".format(akar))

    x_vals = np.linspace(x1 - 0.5, x2 + 0.5, 400)
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)", color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(akar, color='red', linestyle='--', label=f"Akar ≈ {akar:.5f}")
    plt.title("Metode Regula Falsi")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
