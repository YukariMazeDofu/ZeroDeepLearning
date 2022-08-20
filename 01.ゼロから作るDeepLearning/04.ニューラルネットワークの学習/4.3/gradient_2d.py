def function_2(x): return x[0]**2 + x[1]**2  # == np.sum(x**2)
def numerical_diff(f, x): return (f(x + 1e-4) - f(x - 1e-4)) / (2e-4)


def function_2_x1_4(x0): return x0**2 + 4**2
def function_2_x0_3(x1): return 3**2 + x1**2


print(numerical_diff(function_2_x1_4, 3))
print(numerical_diff(function_2_x0_3, 4))
