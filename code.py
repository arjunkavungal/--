from scipy.misc import derivative
def f(x):
    return x**3 + x**2
st.write(derivative(f, 1.0, dx=1e-6))
